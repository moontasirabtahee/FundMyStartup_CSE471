from django.urls import path
from . import views
urlpatterns = [
    path('chats', views.messages_page, name='chats'),
]