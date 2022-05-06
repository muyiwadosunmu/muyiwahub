from django.urls import path
from . import views
from rest_framework import permissions


urlpatterns = [
     # path('', views.getRoutes),
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>/', views.getRoom)
]