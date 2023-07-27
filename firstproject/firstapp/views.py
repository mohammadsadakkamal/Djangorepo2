from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    print("Hi this is django")
    s="<h1>Dont feel difficult....Just it is first time feeling... really django is very esay if u practice then you see</h1>"
    return HttpResponse(s)
