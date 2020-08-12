from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return HttpResponse("VUMC rocks!!")
def view1(response):
    return HttpResponse("Another page") 