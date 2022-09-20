from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed

# Create your views here.
def index(request):
    return HttpResponse('hola a todos')

def newmember(request):
    if request.method == 'POST':
        return HttpResponse('agregar cliente')
    else:
        return HttpResponseNotAllowed(['POST'],'metodo invalido')

def getmember(request):
    if request.method == 'GET':
        return HttpResponse('leer informacion')
    else:
        return HttpResponseNotAllowed(['GET'],'metodo invalido')

