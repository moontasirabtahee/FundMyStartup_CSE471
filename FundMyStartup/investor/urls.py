from django.urls import path
from . import views

urlpatterns = [
    path('', views.investPro, name='investor-index'),
    ]