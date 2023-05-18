"""sjtuers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from . import views, settings

urlpatterns = [
    path('', views.index_view),
    path('admin/', admin.site.urls),
    path('index/', include('index.urls')),
    path('weather/', include('weather.urls')),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('logged_out', views.logged_out, name='logged_out'),
    path('authorize/', views.authorize, name='authorize'),
    path('about/', include('about.urls')),
    re_path(r'media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]

