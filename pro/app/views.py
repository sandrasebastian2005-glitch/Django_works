from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# function based

def Home(request):
    print(request.method)
    if (request.method=="GET"):
        return HttpResponse("Welcome To Django")

def Index(request):
    if (request.method=='GET'):
        return HttpResponse("Index")
# with just this we cannot see this in localhost 
# we have to do the connection of url path in urls.py