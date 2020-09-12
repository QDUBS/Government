from django.urls import path
from .views import Register, DashBoard






urlpatterns = [
    path('register/', Register, name = 'register'),
    path('dashboard/', DashBoard, name = 'dashboard'),
]
