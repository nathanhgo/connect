from django.urls import path
from .views import ping_pong_test

urlpatterns = [
    path('ping/', ping_pong_test, name='ping_pong'),
]