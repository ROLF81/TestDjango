from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index, name = 'indice'),
    path('add', views.newmember, name = 'Nmember'),
    path('get', views.getmember, name = 'Gmember'),

]
