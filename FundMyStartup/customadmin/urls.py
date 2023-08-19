from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [

    path('adminLogin/', views.adminLogin, name='adminLogin'),
    path('adminDashboard/', views.adminDashboard, name='adminDashboard'),
    path('/adminLogout/', views.adminLogout, name='adminLogout'),
]