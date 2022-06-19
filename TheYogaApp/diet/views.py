from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse


#Create your views here.
def diet(request):
    return render(request, 'diet/diet.html')


def tips(request):
    return render(request, 'diet/tips.html')


def diabetes(request):
    return render(request, 'diet/diabetes.html')


def arthritis(request):
    return render(request, 'diet/arthritis.html')

# def page_by_problem(request, problem):
#     if problem == 'diabetes':
#         return render(request, 'diet/diabetes.html')
#     else:
#         return render(request, 'diet/arthritis.html')

