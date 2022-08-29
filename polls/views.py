from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Hola, mundo. Estás en la app de polls (no me acuerdo como se dice polls en ingles)")
