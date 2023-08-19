from django.urls import path
from . import views

urlpatterns = [

    path('startup', views.Createstartup, name='startup'),
    path('entrepreneur_Profile', views.entreprePro, name='entreprePro'),
]