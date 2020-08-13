from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework.parsers import JSONParser
from .models import PheWasModel
from .serializers import PhewasSerializer

# Create your views here.


def PheWas_List(request):
    if request.method =='GET':
        phewas = PheWasModel.objects.all()
        serializer = PhewasSerializer(phewas,many=True)
        return JsonResponse(serializer.data, safe=False)
        


def index(response):
    return HttpResponse("VUMC rocks!!")
def view1(response):
    return HttpResponse("Another page") 