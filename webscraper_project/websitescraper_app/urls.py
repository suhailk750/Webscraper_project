from django.http import HttpResponse
from . import views
from django.urls import path

# app_name='movieapp'
urlpatterns = [

    path('',views.home,name='home'),

]