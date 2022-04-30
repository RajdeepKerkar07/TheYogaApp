from django.shortcuts import render

from .models import Asana
from ..users.models import Profile


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    asana = Asana.objects.all()
    profile = Profile.objects.all()
    return render(request, 'dashboard.html', {'asana': asana, 'profile': profile})

