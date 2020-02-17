from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.keyboard),
    path('message',views.message),
]