from django.contrib import admin
from django.urls import path,re_path
from f_goods.views import *

urlpatterns = [
    re_path('list_(\d+)_(\d+)_(\d+)$',typelist),
    re_path('(\d+)',detail),
    path('', index, name='index'),
]
