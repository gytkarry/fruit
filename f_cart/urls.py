from django.contrib import admin
from django.urls import path
from f_goods.views import index

urlpatterns = [
    path('', index, name='index'),
]
