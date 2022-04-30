from django.shortcuts import render

from .models import Asana


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    asana = Asana.objects.all()
    return render(request, 'dashboard.html', {'asana': asana})

