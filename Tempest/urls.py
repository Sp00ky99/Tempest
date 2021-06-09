from django.contrib import admin

from django.urls import path
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('index',views.index, name='index'),
    path('map',views.map, name='map'),
    path('list',views.list, name='list'),
    path('about',views.about, name='about'),
    path('info',views.info, name='info'),


]
