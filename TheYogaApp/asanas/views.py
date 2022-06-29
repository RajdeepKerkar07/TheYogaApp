from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Asana
import os
from django.conf import settings


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/users/login/')
def dashboard(request):
    asana = Asana.objects.all()
    return render(request, 'dashboard.html', {'asana': asana})


@login_required(login_url='/dashboard/')
def yoga(request):
    return render(request, 'yoga.html')
