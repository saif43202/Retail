from django.contrib import admin
from django.urls import path
from RetailApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup),
    path('login/',login),
    path('savesignup/',savesignup),
    path('savelogin/',savelogin),
    path('main/',main),
    path('showdata/',showdata),
    path('index/',index),
    path('select/',select),
    path('showproduct/',showproduct),
    path('showcat/',showcat),
    path('logout/',logout),
]
