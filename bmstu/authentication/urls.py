from django.urls import path
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    # Add more URL patterns as needed
]
