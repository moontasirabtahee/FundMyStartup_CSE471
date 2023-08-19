from django.urls import path
from . import views

urlpatterns = [
    path('startup', views.Createstartup, name='startup'),
    path('', views.entreprePro, name='entrepreneur_Profile'),
]