from django.http import HttpResponse
import json
import requests
from .views import get_json, headers
from rest_framework.views import APIView
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.options.global_options import ThemeType


def canteen():
    url = 'https://canteen.sjtu.edu.cn/CARD/Ajax/Place'
    session = requests.session()
    response = session.get(url=url, headers=headers).text
    return get_json(response)


def lib():
    url = 'https://zgrstj.lib.sjtu.edu.cn/cp?callback=CountPerson'
    session = requests.session()
    response = session.get(url=url, headers=headers).text
    data = json.loads(response[12:-2], strict=False)['numbers']
    return data


def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error
canteen = canteen()
lib = lib()


# 餐厅
def can_bar() -> Bar:
    c = (
        Bar()
            .add_xaxis(["一餐", "一餐清真", "二餐", "三餐", "三餐清真", "四餐", "五餐", "哈乐", "玉兰苑"])
            .add_yaxis("已取餐量",
                       [canteen[0]['Seat_u'], canteen[1]['Seat_u'], canteen[2]['Seat_u'],
                        canteen[3]['Seat_u'], canteen[4]['Seat_u'], canteen[5]['Seat_u'],
                        canteen[6]['Seat_u'], canteen[7]['Seat_u'], canteen[8]['Seat_u']],
                       category_gap="30%"
                       )
            .add_yaxis("供应总量",
                       [canteen[0]['Seat_s'], canteen[1]['Seat_s'], canteen[2]['Seat_s'],
                        canteen[3]['Seat_s'], canteen[4]['Seat_s'], canteen[5]['Seat_s'],
                        canteen[6]['Seat_s'], canteen[7]['Seat_s'], canteen[8]['Seat_s']],
                       category_gap="30%"
                       )
            # rotate 旋转角度
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30, interval=0, font_size=10)),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=7)))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            # .reversal_axis()
            .dump_options_with_quotes()
    )
    return c


def lib_bar() -> Bar:
    b = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(["图书馆主馆", "李政道图书馆", "包玉刚图书馆", "徐汇社科馆"])
            .add_yaxis("在馆人数", [lib[0]['inCounter'], lib[1]['inCounter'], lib[2]['inCounter'], lib[3]['inCounter']],
                       category_gap="30%", stack='stack1'
                       )
            .add_yaxis("可容纳人数", [lib[0]['max'], lib[1]['max'], lib[2]['max'], lib[3]['max']],
                       category_gap="30%",
                       stack='stack1'
                       )
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-20, interval=0, font_size=11)))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            # .set_series_opts(label_opts=opts.LabelOpts(position='right', font_size = 16)
            .dump_options_with_quotes()
    )
    return b


class ChartViewCanteen(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(can_bar()))


class IndexViewCanteen(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./templates/canteen.html").read())


class ChartViewLibrary(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(lib_bar()))


class IndexViewLibrary(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./templates/library.html").read())