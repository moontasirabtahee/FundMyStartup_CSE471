from django.urls import path
from . import views
urlpatterns = [
    path("",views.home),

    path("home/",views.home,name="home"),
    path("chat/<str:room_name>/",views.room,name="room_name")


]