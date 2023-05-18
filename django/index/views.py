from django.http import HttpResponse
from django.shortcuts import render
from .models import Site, SimpleMode, User, Wallpaper, Countdown
import urllib.request

import requests
import asyncio
import aiohttp
import json
import datetime

from lxml import etree
from urllib.parse import quote
from asyncio.proactor_events import _ProactorBasePipeTransport
from functools import wraps

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
}


def index_view(request):
    city = get_city(request)
    names = [
        'jwc',
        'jnews',
        # 'weather',
        'weibo',
        'zhihu',
        'bilibili',
        # 'corona',
        'poem',
    ]
    urls = [
        'https://jwc.sjtu.edu.cn/xwtg/tztg.htm',
        'https://www.sjtu.edu.cn/',
        # 'http://wthrcdn.etouch.cn/WeatherApi?city=' + quote(city),
        # 'https://tenapi.cn/resou/',
        # 'https://tenapi.cn/zhihuresou/',
        'https://tophub.today/n/KqndgxeLl9',
        'https://tophub.today/n/mproPpoq6O',
        'https://api.bilibili.com/x/web-interface/popular?ps=5&pn=1',
        # 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf',
        'https://v1.jinrishici.com/all.json'
    ]
    urls_names = dict(zip(urls, names))
    responses = {}

    # 异步编程
    async def fetch(session, url):
        async with session.get(url=url, headers=headers) as response:
            assert response.status == 200
            page_text = await response.text()
            url = str(response.url)
            name = urls_names[url]
            responses[name] = page_text

    async def main():
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64, verify_ssl=False)) as session:
            tasks = [asyncio.create_task(fetch(session, url)) for url in urls]
            await asyncio.wait(tasks)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

    # 初始化default用户
    jaccount_default_flag = User.objects.filter(jaccount='000')
    if not jaccount_default_flag:
        User.objects.create(jaccount='000')
        user = User.objects.filter(jaccount='000')[0]
        SimpleMode.objects.create(user=user)
        Wallpaper.objects.create(user=user)
        Countdown.objects.create(user=user)
        initialize_site(user)

    try:
        result_origin = jac(request)
        result = result_origin['entities'][0]['name']
        jaccount = result_origin['entities'][0]['account']
        jaccount_flag = User.objects.filter(jaccount=jaccount)

        # 如果这个Jac用户第一次登录，则在数据库的User表中新建一条记录
        # 并且复制default用户的所有网站，作为初始设置
        if not jaccount_flag:
            User.objects.create(user_name=result, jaccount=jaccount)
            user = User.objects.filter(jaccount=jaccount)[0]
            SimpleMode.objects.create(user=user, username=result, is_active=False)
            Wallpaper.objects.create(user=user, username=result)
            Countdown.objects.create(user=user, username=result)
            user_site_flag = Site.objects.filter(user='000')
            for site in user_site_flag:
                Site.objects.create(site_name=site.site_name, site_url=site.site_url, site_src=site.site_src, user=user,
                                    is_active=site.is_active)

        user = User.objects.filter(jaccount=jaccount)[0]
        simple_mode_flag = SimpleMode.objects.filter(user=jaccount)[0]
        simple_mode = {'username': result, 'is_active': simple_mode_flag.is_active}
        wallpaper_flag = Wallpaper.objects.filter(user=jaccount)[0]
        wallpaper = {'username': result,
                     'photo_url': '../media/wallpaper/' + wallpaper_flag.photo_name,
                     'photo_name': wallpaper_flag.photo_name,
                     'css': wallpaper_flag.css}

        countdown_flag = Countdown.objects.filter(user=jaccount)
        countdown_flag = Countdown.objects.filter(user=jaccount)[0]

        countdown = compute_countdown(countdown_flag.date_name, countdown_flag.year,
                                      countdown_flag.month, countdown_flag.day)
    except:
        result = ''
        jaccount = '000'
        user = User.objects.filter(jaccount='000')[0]
        simple_mode = {'username': 'visitor', 'is_active': False}
        wallpaper = {'username': "visitor",
                     'photo_url': '../media/wallpaper/visitor.jpg',
                     'photo_name': 'visitor.jpg',
                     "css": "linear-gradient(90deg, #70e1f5 0%, #ffd194 100%)"}
        countdown = compute_countdown("元旦", 2023, 1, 1)
        print(f"Please login!")
        print("except!")

    request.session['jaccount'] = jaccount
    sites_object = Site.objects.filter(user=jaccount, is_active=True)
    sites = []
    for site in sites_object:
        site_json = {'site_name': site.site_name, 'site_url': site.site_url, 'site_src': site.site_src, 'is_active': site.is_active}
        sites.append(site_json)
    print(sites)

    # 对爬取内容进行获取，如果由于获取数据结构变化而导致不能正常获取，则获取信息为报错信息
    try:
        jwc_data = jwc(responses['jwc'])
    except Exception as e:
        jwc_data = [{"title": "教务处信息获取失败，请联系管理员！", "url": ""}]
    try:
        jnews_data = jnews(responses['jnews'])
    except Exception as e:
        jnews_data = [{"title": "交大新闻信息获取失败，请联系管理员！", "url": ""}]
    # try:
    #     weather_data = weather(responses['weather'])
    # except Exception as e:
    #     weather_data = ["天气信息获取失败，请联系管理员！"]
    try:
        weibo_data = weibo(responses['weibo'])
    except Exception as e:
        weibo_data = [{"name": "微博信息获取失败，请联系管理员！", "url": "", "hot": ""}]
    try:
        zhihu_data = zhihu(responses['zhihu'])
    except Exception as e:
        zhihu_data = [{"name": "知乎信息获取失败，请联系管理员！", "url": ""}]
    try:
        bilibili_data = bilibli(responses['bilibili'])
    except Exception as e:
        bilibili_data = [{"title": "bilibili信息获取失败，请联系管理员！", "url": "", "view": ""}]
    # try:
    #     corona_data = corona(responses['corona'])
    # except Exception as e:
    #     corona_data = {'lastUpdateTime': '疫情数据获取失败，请联系管理员',
    #                    'chinaTotal': {'dead': "Error", 'importedCase': "Error", 'heal': "Error", 'nowConfirm': "Error",
    #                                   'noInfectH5': "Error", 'confirm': "Error", 'suspect': "Error"},
    #                    'chinaAdd': {'dead': 0, 'importedCase': 0, 'heal': 0, 'nowConfirm': 0,
    #                                   'noInfectH5': 0, 'confirm': 0, 'suspect': 0}}
    try:
        poem_data = poem(responses['poem'])
    except Exception as e:
        poem_data = {'content': "诗句信息获取失败，请联系管理员！", 'origin': '', 'author': '', 'category': ''}

    locals = {
        'jwc': jwc_data,
        'jnews': jnews_data,
        # 'weather': weather_data,
        'weibo': weibo_data,
        'zhihu': zhihu_data,
        'bilibili': bilibili_data,
        # 'corona': corona_data,
        'poem': poem_data,
        'sites': sites,
        'jac': result,
        'simple_mode': simple_mode,
        "wallpaper": wallpaper,
        'countdown': countdown,
    }
    print(locals)
    return HttpResponse(json.dumps(locals), content_type="application/json")


# 按字符实际长度截取，一个汉字长度为2，一个字母/数字长度为1
def cut_str(str_before, len_cut):
    to_bytes = str_before.encode('utf-8')
    cut_tmp = to_bytes[:len_cut]
    cut_res = cut_tmp.decode('utf-8', errors='ignore')  # 按bytes截取时有小部分无效的字节，传入errors='ignore'忽略错误
    return cut_res


def get_json(response):
    data = json.loads(response, strict=False)
    return data


def get_html(response):
    return response


def jwc(response):
    html = get_html(response)
    tree = etree.HTML(html)
    a_list = tree.xpath('//div[@class="wz"]/a')
    jwc_dic = []
    for i in range(5):
        title = str(i + 1) + ' ' + a_list[i].xpath('./h2/text()')[0]
        if len(title.encode('utf-8')) > 55:
            title = cut_str(title, 53) + '...'
        url = 'https://jwc.sjtu.edu.cn' + a_list[i].xpath('./@href')[0][2:]
        dic = {'title': title, 'url': url}
        jwc_dic.append(dic)
    return jwc_dic


def jnews(response):
    html = get_html(response)
    tree = etree.HTML(html)
    a_list = tree.xpath('//div[@class="new-add-list  clearfix"]//ul[1]//a')
    jnews_dic = []
    for i in range(5):
        title = str(i + 1) + ' ' + a_list[i].xpath('./text()')[0]
        if len(title.encode('utf-8')) > 55:
            title = cut_str(title, 53) + '...'
        url = a_list[i].xpath('./@href')[0]
        dic = {'title': title, 'url': url}
        jnews_dic.append(dic)
    return jnews_dic


def bilibli(response):
    bilibili_json = get_json(response)['data']['list']
    bilibili = []
    for i in range(5):
        dic = {'title': str(i + 1) + ' ' + bilibili_json[i]['title']}
        if len(dic['title'].encode("utf-8")) > 46:
            dic['title'] = cut_str(dic['title'], 44) + '...'
        dic['url'] = bilibili_json[i]['short_link']
        dic['view'] = bilibili_json[i]['stat']['view']
        bilibili.append(dic)
    return bilibili

# 从公开API获取的函数
# def weibo(response):
#     data = get_json(response)['list']
#     weibo_dict = []
#     for i in range(5):
#         name = data[i]['name']
#         name = str(i + 1) + ' ' + name
#         if len(name.encode('utf-8')) > 46:
#             name = cut_str(name, 44) + '...'
#         url = data[i]['url']
#         hot = data[i]['hot']
#         weibo_item = {'name': name, 'url': url, 'hot': hot}
#         weibo_dict.append(weibo_item)
#     return weibo_dict


# def zhihu(response):
#     data = get_json(response)['list']
#     zhihu_dict = []
#     for i in range(5):
#         name = data[i]['query']
#         name = str(i + 1) + ' ' + name
#         if len(name.encode('utf-8')) > 55:
#             name = cut_str(name, 53) + "..."
#         url = data[i]['url']
#         zhihu_item = {'name': name, 'url': url}
#         zhihu_dict.append(zhihu_item)
#     return zhihu_dict

# 代理网站爬取的函数
def weibo(response):
    html = get_html(response)
    tree = etree.HTML(html)
    tr_list = tree.xpath('//table/tbody/tr')[:5]
    weibo_dict = []
    for i in range(len(tr_list)):
        name = tr_list[i].xpath('./td[2]/a/text()')[0]
        url = 'https://s.weibo.com/weibo?q=%23' + name + "%23"
        name = str(i + 1) + ' ' + name
        if len(name.encode('utf-8')) > 46:
            name = cut_str(name, 44) + '...'
        hot = tr_list[i].xpath('./td[3]/text()')[0]
        weibo_item = {'name': name, 'url': url, 'hot': hot}
        weibo_dict.append(weibo_item)
    return weibo_dict


def zhihu(response):
    html = get_html(response)
    tree = etree.HTML(html)
    tr_list = tree.xpath('//tbody/tr')[:5]
    zhihu_dict = []
    for i in range(len(tr_list)):
        name = tr_list[i].xpath('./td[@class="al"]/a/text()')[0]
        url = 'https://tophub.today' + tr_list[i].xpath('./td[@class="al"]/a/@href')[0]
        name = str(i + 1) + ' ' + name
        if len(name.encode('utf-8')) > 55:
            name = cut_str(name, 53) + "..."
        zhihu_item = {'name': name, 'url': url}
        zhihu_dict.append(zhihu_item)
    return zhihu_dict


def weather(response):
    data = get_html(response)
    parser = etree.XMLParser(resolve_entities=False, strip_cdata=False, recover=True, ns_clean=True)
    XML_tree = etree.fromstring(data.encode(), parser=parser)

    forecast_list = XML_tree.xpath('//forecast/weather')
    forecast_dic = {}
    for i in range(len(forecast_list)):
        day_name = 'day' + str(i)
        forecast_dic[day_name] = {}
        forecast_dic[day_name]['date'] = '周' + forecast_list[i].xpath('./date/text()')[0][-1]
        forecast_dic[day_name]['high'] = forecast_list[i].xpath('./high/text()')[0][-3:-1]
        forecast_dic[day_name]['low'] = forecast_list[i].xpath('./low/text()')[0][-3:-1]
        forecast_dic[day_name]['type'] = forecast_list[i].xpath('.//type/text()')[0]
    forecast_dic['day0']['date'] = '今天'

    weather_dict = {
        'city': XML_tree.xpath('//city/text()')[0],
        'wendu': XML_tree.xpath('//wendu/text()')[0],
        'forecast': forecast_dic,
    }
    return weather_dict

#
# def corona(response):
#     data = get_json(response)['data']["diseaseh5Shelf"]
#     del data["areaTree"]
#     return data


def poem(response):
    return get_json(response)


def jac(request):
    token = request.session['token']
    access_token = token['access_token']
    requests.packages.urllib3.disable_warnings()
    result = requests.get(f'https://api.sjtu.edu.cn/v1/me/profile?access_token={access_token}', verify=False)
    return result.json()


def compute_countdown(date_name, year, month, day):
    d1 = datetime.date.today()
    d2 = datetime.date(year, month, day)
    interval = d2 - d1
    countdown = {'date_name': date_name, "interval": interval.days}
    return countdown


def get_city(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    else:
        user_ip = request.META.get('REMOTE_ADDR')
    url = 'http://ip-api.com/json/' + user_ip + '?lang=zh-CN&fields=city'
    response = urllib.request.urlopen(url)
    html = json.loads(response.read())
    try:
        city = html["city"]
    except Exception as e:
        city = '闵行'
    return city


def initialize_site(user):
    Site.objects.create(site_name='Canvas',site_url='https://oc.sjtu.edu.cn/', site_src='../static/img/site_icon/在线课程.png', user=user)
    Site.objects.create(site_name='教学信息', site_url='https://i.sjtu.edu.cn/', site_src='../static/img/site_icon/教学信息.png', user=user)
    Site.objects.create(site_name='学生事务', site_url='https://affairs.sjtu.edu.cn/', site_src='../static/img/site_icon/学生事务.png', user=user)
    Site.objects.create(site_name='交我办', site_url='https://my.sjtu.edu.cn/', site_src='../static/img/site_icon/交我办.png', user=user)
    Site.objects.create(site_name='交大官网', site_url='https://www.sjtu.edu.cn/', site_src='../static/img/site_icon/官网.png', user=user)
    Site.objects.create(site_name='研究生院', site_url='https://www.gs.sjtu.edu.cn/', site_src='../static/img/site_icon/研究生网.png', user=user)
    Site.objects.create(site_name='交大邮箱', site_url='https://mail.sjtu.edu.cn/', site_src='../static/img/site_icon/邮箱.png', user=user)
    Site.objects.create(site_name='交大云盘', site_url='https://jbox.sjtu.edu.cn/', site_src='../static/img/site_icon/交大云盘.png', user=user)
    Site.objects.create(site_name='水源社区', site_url='https://shuiyuan.sjtu.edu.cn/', site_src='../static/img/site_icon/水源.png', user=user)
    Site.objects.create(site_name='䇹政项目', site_url='https://chuntsung.sjtu.edu.cn/', site_src='../static/img/site_icon/䇹政.png', user=user)
    Site.objects.create(site_name='创新实践', site_url='https://uitp.sjtu.edu.cn/', site_src='../static/img/site_icon/大创.png', user=user)
    Site.objects.create(site_name='教学楼', site_url='https://ids.sjtu.edu.cn/', site_src='../static/img/site_icon/教学楼.png', user=user)
    Site.objects.create(site_name='图书馆', site_url='https://www.lib.sjtu.edu.cn/', site_src='../static/img/site_icon/图书馆.png', user=user)
    Site.objects.create(site_name='选课社区', site_url='https://course.sjtu.plus/', site_src='../static/img/site_icon/选课社区.png', user=user)
    Site.objects.create(site_name='github', site_url='https://github.com/', site_src='https://files.codelife.cc/itab/search/github.svg', user=user)
    Site.objects.create(site_name='bilibili', site_url='https://bilibili.com/', site_src='https://files.codelife.cc/itab/search/bilibili.svg', user=user)
    Site.objects.create(site_name='知乎', site_url='https://www.zhihu.com/', site_src='https://files.codelife.cc/itab/search/zhihu.svg', user=user)
    Site.objects.create(site_name='豆瓣', site_url='https://www.douban.com/', site_src='https://files.codelife.cc/itab/search/douban.svg', user=user)
    Site.objects.create(site_name='淘宝', site_url='https://www.taobao.com/', site_src='https://www.taobao.com/favicon.ico', user=user)
    Site.objects.create(site_name='爱奇艺', site_url='https://www.iqiyi.com/', site_src='https://www.iqiyi.com/favicon.ico', user=user)
    Site.objects.create(site_name='一个木函', site_url='https://web.woobx.cn/', site_src='https://web.woobx.cn/favicon.ico', user=user)
    Site.objects.create(site_name='百度', site_url='https://www.baidu.com/', site_src='https://www.baidu.com/favicon.ico', user=user, is_active=False)
    Site.objects.create(site_name='搜狗', site_url='https://www.sogou.com/', site_src='https://www.sogou.com/favicon.ico', user=user, is_active=False)


def silence_event_loop_closed(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except RuntimeError as e:
            if str(e) != 'Event loop is closed':
                raise

    return wrapper


_ProactorBasePipeTransport.__del__ = silence_event_loop_closed(_ProactorBasePipeTransport.__del__)
