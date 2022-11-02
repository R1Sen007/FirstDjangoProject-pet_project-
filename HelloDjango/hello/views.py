from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    # return HttpResponse("<h2>Main page</h2>")
    return render(request, "index2.html")

def postuser(request):
    name = request.POST.get("name", "undefined")
    age = request.POST.get("age", "undefined")
    return HttpResponse(f"<h2>NAME: {name} <br> AGE: {age}</h2>")

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

def user(request):
    age = request.GET.get("age", "Undefined")
    name = request.GET.get("name", "Undefined")
    return HttpResponse(f"<h2>NAME: {name} <br> AGE: {age}</h2>")