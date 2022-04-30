from django.shortcuts import render

# Create your views here.
def nutritionist(request):
    return  render(request, 'nutritionist.html')