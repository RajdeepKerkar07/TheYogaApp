from django.shortcuts import render

from .models import Diet


def diet(request):
    return render(request, 'diet/diet.html')


def page_by_problem(request, problem_name):
    diet = Diet.objects.get(problem__name__iexact=problem_name)
    return render(request, 'diet/problem_tips.html', context={'diet': diet})


def me(request):
    return render(request, 'diet/profile.html')
