from django.urls import path,include
from . import views


urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
    path('logout', views.logout, name='logout'),


]