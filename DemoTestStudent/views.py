from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vw_demostudent(request):
    return HttpResponse("Hi This is my first Azure Application Hosts")