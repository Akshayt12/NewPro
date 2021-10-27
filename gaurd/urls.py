"""gaurd URL Configuration"""
from django.urls import path
from . import views
urlpatterns = [
    path('',views.gaurd,name='gaurd'),
    path('glogin',views.glogin,name='glogin'),
    path('ghome',views.ghome,name='ghome'),
    path('glogout',views.glogout,name='glogout'),
    path('enter',views.enter,name='enter'),
    path('insert_entry',views.insert_entry,name='insert_entry'),
    path('chk_entries',views.chk_entries,name='chk_entries'),
    path('exit',views.exit,name='exit'),
    path('update_exit',views.update_exit,name='update_exit'),
]
