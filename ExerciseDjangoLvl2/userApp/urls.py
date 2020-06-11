from django.shortcuts import render
from django.urls import path
from userApp import views

urlpatterns = [
    path('',views.user, name="user"),
]