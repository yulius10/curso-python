from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return HttpResponse('hola mundo desde Django')

def despedirse(request):
    return HttpResponse('despedida desde Django')