from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework.parsers import JSONParser
from .models import PheWasModel,PheWasModel_2
from .serializers import PhewasSerializer,PhewasSerializer2

# Create your views here.


def PheWas_List(request):
    if request.method =='GET':
        phewas = PheWasModel.objects.all()
        serializer = PhewasSerializer(phewas,many=True)
        return JsonResponse(serializer.data, safe=False)

     
def PheWas_List_2(request):
    if request.method =='GET':
        phewas2 = PheWasModel_2.objects.all()
        serializer2 = PhewasSerializer2(phewas2,many=True)
        return JsonResponse(serializer2.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer2 = PhewasSerializer2(data=data)
        if serializer2.is_valid():
            serializer2.save()
            return JsonResponse(serializer2.data, status=201)
        return JsonResponse(serializer2.errors, status=400)

def index(response):
    return HttpResponse("VUMC rocks!!")
def view1(response):
    return HttpResponse("Another page") 