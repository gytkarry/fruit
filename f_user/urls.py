from django.contrib import admin
from django.urls import path
from f_user.views import *

from  . import views
urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.register),
    path('reg',views.register_handle),
    path('log',views.login_handle),
    path('logout',views.logout),
    path('check_name',register_exist),
    path('userinfo',user_center_info),
    path('userupdate',userupdate),
    path('shdz',shdz),
    path('add_save',add_save),
    path('mrdz',mrdz),
    path('scdz',scdz),
    path('bjdz',bjdz),
]
