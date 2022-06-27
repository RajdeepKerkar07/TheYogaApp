from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.me),
    path('<str:problem_name>/', views.page_by_problem),
    path('', views.diet, name='diet'),
]
