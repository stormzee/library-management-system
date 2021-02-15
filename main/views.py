from django.shortcuts import render, HttpResponse

from .models import Category

# Create your views here.

def index(request):
    return render(request, 'index.html')

