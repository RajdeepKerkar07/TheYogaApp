from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('asanas.urls')),
    path('users/', include('users.urls')),
    path('diet/', include('diet.urls')),
    path('admin/', admin.site.urls),
]
