from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from . import views, axios

urlpatterns = [
    # get请求：view.py
    path('', views.index_view, name='index'),
    path('test/', views.test_view, name='test'),
    path('scrapy/', views.scrap_view, name='scrapy'),
    path('data/', views.data_view, name="data"),
    # post请求：axios.py
    path('add_site/', axios.add_site, name="add_site"),
    path('refactor_site/', axios.refactor_site, name="refactor_site"),
    path('delete_site/', axios.delete_site, name="delete_site"),
    path('simple_mode/', axios.simple_mode, name="simple_mode"),
    path('add_task/', axios.add_task, name="add_task"),
    path('delete_task/', axios.delete_task, name="delete_task"),
    path('done_task/', axios.done_task, name="done_task"),
    path('aidraw/', axios.ai_draw, name="aidraw"),
    path('upload_img/', csrf_exempt(axios.img_upload), name="uploda_img"),
    path('color_wallpaper/', axios.color_wallpaper, name="color_wallpaper"),
]
