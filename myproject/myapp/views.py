from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from . models import Members
import json

# Create your views here.
def index(request):
    return HttpResponse('hola a todos')

def newmember(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            member = Members(
                name = data["name"],
                email = data ["email"]
            )
            member.save()
            return HttpResponse('agregar cliente')
        except:
            return HttpResponseBadRequest('error en los datos enviados')
    else:
        return HttpResponseNotAllowed(['POST'],'metodo invalido')

def getmember(request):
    if request.method == 'GET':
        members = Members.objects.all()
        data = []
        for i in members:
            dictObject = {'id':i.id, 'name': i.name, 'email': i.email}
            data.append(dictObject)
        datajson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['content-type'] = 'text/json'
        resp.content = datajson
        return resp
    
    else:
        return HttpResponseNotAllowed(['GET'],'metodo invalido')

