from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vw_demostudent(request):
    return HttpResponse("My First View")