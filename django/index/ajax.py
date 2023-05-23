from django.http import JsonResponse, HttpResponse
from urllib.parse import urlparse
import json
from .models import Site, SimpleMode, Wallpaper, User, Task
from .views import get_icon_src


def img_upload(request):
    jaccount = request.session['jaccount']
    file_img = request.FILES['upload_file']  # 获取文件对象
    file_name = request.FILES['upload_file'].name.strip()
    print(file_name)
    if file_name == "":
        return JsonResponse(0, safe=False)

    wallpaper = Wallpaper.objects.filter(user=jaccount)[0]
    wallpaper.photo = file_img
    wallpaper.photo_name = file_name
    wallpaper.css = ""
    wallpaper.save()
    try:
        return JsonResponse(1, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse(0, safe=False)


def add_site(request):
    # jaccount = request.session['jaccount']

    jaccount = request.POST.get('jaccount').strip()
    
    res = {'key': 1}

    user = User.objects.filter(jaccount=jaccount)[0]
    site_count = len(Site.objects.filter(user=jaccount, is_active=True))
    if site_count >= 28:
        res['key'] = 0
        return HttpResponse(json.dumps(res), content_type="application/json")

    site_name = request.POST.get('site_name').strip()
    site_url = request.POST.get('site_url').strip()

    if site_name == "" or site_url == "":
        res['key'] = 3
        return HttpResponse(json.dumps(res), content_type="application/json")

    if not site_url.startswith("http"):
        site_url = "https://" + site_url
    if not site_url.endswith("/"):
        site_url = site_url + "/"
    site = Site.objects.filter(site_url=site_url, user=jaccount)
    # 取主域名
    resp = urlparse(site_url)
    site_url_main = "https://" + str(resp.netloc) + "/"
    if site:
        site[0].site_name = site_name
        site[0].save()
        if not site[0].is_active:
            site[0].is_active = True
            site[0].save()
            res['key'] = 2
            return HttpResponse(json.dumps(res), content_type="application/json")
        res['key'] = 2
        return HttpResponse(json.dumps(res), content_type="application/json")
    
    elif 'sjtu' in site_url:
        site_src = '/dist/assets/site_icon/school.png'
        Site.objects.create(user=user, site_name=site_name, site_url=site_url, site_src=site_src)
    else:
        site_src = get_icon_src(site_url)
        Site.objects.create(user=user, site_name=site_name, site_url=site_url, site_src=site_src)

    res['key'] = 1
    return HttpResponse(json.dumps(res), content_type="application/json")


def refactor_site(request):
    # jaccount = request.session['account']
    # 从前端发来的请求中拿到jaccount
    jaccount = request.POST.get('jaccount').strip()
    # print(f"\njaccount:{jaccount}\n")
    site_name = request.POST.get('refactor_site_name').strip()
    site_url = request.POST.get('refactor_site_url').strip()

    # 如果修改成功，则返回1；否则返回0
    res = {'key': 1}

    if site_name == "" or site_url == "":
        res['key'] = 0
    else:
        try:
            for site in Site.objects.filter(user=jaccount, site_url=site_url):
                site.site_name = site_name
                site.save()
        except:
            res['key'] = 0

    return HttpResponse(json.dumps(res), content_type="application/json")
    # return JsonResponse(1, safe=False)


def delete_site(request):
    # jaccount = request.session['jaccount']
    jaccount = request.POST.get('jaccount').strip()
    delete_site_name = request.POST.get('delete_site_name').strip()

    # 如果删除成功，则返回1；否则返回0
    res = {'key': 1}
    try:
        for site in Site.objects.filter(user=jaccount, site_name=delete_site_name):
            site.is_active = False
            site.save()
    except:
        res['key'] = 0
    return HttpResponse(json.dumps(res), content_type="application/json")


def simple_mode(request):
    jaccount = request.session['jaccount']
    this_simple_mode = SimpleMode.objects.get(user=jaccount)
    is_active = request.POST.get('simple_mode_is_active')
    is_active = (is_active == "true")
    this_simple_mode.is_active = is_active
    this_simple_mode.save()
    return HttpResponse("已保存")


def color_wallpaper(request):
    jaccount = request.session['jaccount']
    wallpaper = Wallpaper.objects.filter(user=jaccount)[0]
    css = request.POST.get('css')
    wallpaper.css = css
    wallpaper.save()
    return HttpResponse("已保存")

# def refactor_countdown(request):
#     jaccount = request.session['jaccount']
#     date_name = request.POST.get('refactor_date_name').strip()
#
#     if date_name == "":
#         return JsonResponse(0, safe=False)
#
#     year = request.POST.get('year')
#     month = request.POST.get('month')
#     day = request.POST.get('day')
#     countdown = Countdown.objects.filter(user=jaccount)[0]
#     countdown.date_name = date_name
#     countdown.year = int(year)
#     countdown.month = int(month)
#     countdown.day = int(day)
#     countdown.save()
#
#     this_simple_mode = SimpleMode.objects.get(user=jaccount)
#     this_simple_mode.is_active = True
#     this_simple_mode.save()
#     return JsonResponse(1, safe=False)
