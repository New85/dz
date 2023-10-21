
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(reguest):
    return HttpResponse('страница про фильм')