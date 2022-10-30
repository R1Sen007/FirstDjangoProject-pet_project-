# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Main page</h2>")

def products(request):
    return HttpResponse("Produsts list")
 
def new(request):
    return HttpResponse("New products")
 
def top(request):
    return HttpResponse("Top products")