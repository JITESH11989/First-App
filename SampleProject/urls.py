from django.conf.urls import url
from  django.urls import  path,include
from django.contrib import admin
from django.conf.urls import  include, url

from MyApp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^idealweight/',views.IdealWeight),
    url('/', views.hello, name='hello'),
]