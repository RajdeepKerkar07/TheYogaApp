from django.urls import path
from . import views

urlpatterns = [
    path('arthritis/', views.diabetes, name='arthritis'),
    path('diabetes/', views.diabetes, name='diabetes'),
    path('tips/', views.tips, name='tips'),
    path('', views.diet, name='diet'),

]

# urlpatterns = [
#     path('<problem>', views.page_by_problem),
# ]