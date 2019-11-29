from django.shortcuts import render
from django.urls import path
from .import views

urlpatterns=[
    path('register/',views.reg.as_view(),name="register"),
    path('',lambda request:render(request,'home.html'),name='home')


]