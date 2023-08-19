from django.urls import path
from . import views
urlpatterns = [
    path('chatss', views.messages_page, name='chatss'),
]