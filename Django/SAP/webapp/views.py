from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona

#administrar objects de la clase persona
#https://docs.djangoproject.com/en/3.0/topics/db/managers/
#hacer querys
#https://docs.djangoproject.com/en/3.0/topics/db/queries/

# Create your views here.
def bienvenido(request):
    #return HttpResponse('hola mundo desde Django')
    mensajes = {
        'msg1':'Valor mensaje 1',
        'msg2':'Valor mensaje 2'
    }
    #return render(request,'bienvenido.html',mensajes)
    no_persona = Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    return render(request, 'bienvenido.html',{'no_personas':no_persona,'personas':personas})