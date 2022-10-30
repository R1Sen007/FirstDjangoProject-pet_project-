# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Main page</h2>")

def products(request):
    return HttpResponse("Produsts list")

def product(request, id):
    return HttpResponse(f"Product №{id}")
 
def new(request):
    return HttpResponse("New products")
 
def top(request):
    return HttpResponse("Top products")

def comments(request, id):
    return HttpResponse(f"Comments about product №{id}")

def questions(request, id):
    return HttpResponse(f"Questions about product №{id}")