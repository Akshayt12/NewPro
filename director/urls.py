"""director URL Configuration"""
from django.urls import path
from . import views
urlpatterns = [
    path('',views.director,name='director'),
    path('dlogin',views.dlogin,name='dlogin'),
    path('home',views.home,name='home'),
    path('account',views.account,name='account'),
    path('create_account',views.create_account,name='create_account'),
    path('logout',views.logout,name='logout'),
    path('check',views.check,name='check'),
]
