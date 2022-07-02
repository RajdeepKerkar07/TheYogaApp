from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Asana
from users.models import Profile


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/users/login/')
def dashboard(request):
    asana = Asana.objects.all()
    uid = request.user.id
    c_user = Profile.objects.get(user_id=uid)
    diet = c_user.diet.all()
    return render(request, 'dashboard.html', {'asana': asana, 'diet': diet})


@login_required(login_url='/dashboard/')
def yoga(request):
    return render(request, 'yoga.html')
