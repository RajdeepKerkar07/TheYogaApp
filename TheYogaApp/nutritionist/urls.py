from django.urls import path
from . import views


urlpatterns = [
    path('nutritionist/', views.nutritionist, name='nutritionist'),
]