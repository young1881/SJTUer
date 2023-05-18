from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from . import views, ajax, visual

urlpatterns = [
    # get请求：view.py
    path('', views.index_view, name='index'),
    # post请求：ajax.py
    path('upload_img/', csrf_exempt(ajax.img_upload), name="uploda_img"),
    path('add_site/', ajax.add_site, name="add_site"),
    path('refactor_site/', ajax.refactor_site, name="refactor_site"),
    path('delete_site/', ajax.delete_site, name="delete_site"),
    path('color_wallpaper/', ajax.color_wallpaper, name="color_wallpaper"),
    path('simple_mode/', ajax.simple_mode, name="simple_mode"),
    path('refactor_countdown/', ajax.refactor_countdown, name="refactor_countdown"),
    # 可视化子页面：visual.py
    path('bar', visual.ChartViewCanteen.as_view(), name='can_bar'),
    path('can_index', visual.IndexViewCanteen.as_view(), name='can_index'),
    path('lib_bar', visual.ChartViewLibrary.as_view(), name='lib_bar'),
    path('lib_index', visual.IndexViewLibrary.as_view(), name='lib_index')
]
