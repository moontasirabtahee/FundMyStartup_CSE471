from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.adminLogin, name='admin'),
    path('adminLogin/', views.adminLogin, name='adminLogin'),
    path('/adminDashboard/', views.adminDashboard, name='adminDashboard'),
    path('/adminLogout/', views.adminLogout, name='adminLogout'),
    path('editUser/<int:id>', views.editUser, name='editUser'),
    path('/deleteUser/<int:id>', views.deleteUser, name='deleteUser'),
    path('/deleteFeedback/<int:id>', views.deleteFeedback, name='deleteFeedback'),
    path('/deletestartup/<int:id>', views.deleteStartup, name='deletestartup'),
    path('/editstartup/<int:id>', views.editStartup, name='editstartup'),


]