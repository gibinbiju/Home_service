from django.shortcuts import render
from django.urls import path
from .import views

urlpatterns=[
    path('register/',views.Register,name="register"),
    path('',lambda request:render(request,'home.html'),name='home'),
    path('home',lambda request:render(request,'home.html'),name='home'),
    path('login', views.loginview, name="login"),
    path('logout',views.logoutview,name='logout'),
    path('mypage', lambda request: render(request, 'HSSapp/mypage.html'), name='mypage'),
    path('profile',views.profilecreate,name='profile'),
    path('location',views.locationcreate,name='location'),


]