from django.shortcuts import render
from .models import Asana
import os
from django.conf import settings


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    asana = Asana.objects.all()
    return render(request, 'dashboard.html', {'asana': asana})


def yoga(request):
    return render(request, 'yoga.html')


# file = open(os.path.join(settings.PROJECT_ROOT, 'images/mountain.svg'))
