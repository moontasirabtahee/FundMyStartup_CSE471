from django.urls import path
from . import views

urlpatterns = [
    path('commun', views.commun, name='commun'),
    path('<str:chat>/', views.chat, name='chat'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:chat>/', views.getMessages, name='getMessages'),
]