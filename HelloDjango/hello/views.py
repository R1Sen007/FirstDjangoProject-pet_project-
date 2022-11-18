from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, HttpResponseNotFound
from .models import Person
from .forms import UserForm

def index(request):
    # return HttpResponse("<h2>Main page</h2>")
    # return render(request, "index.html")
    # return render(request, "index2.html")
    # if request.method == "GET":
    #     userform = UserForm()
    #     return render(request, "index3.html", {"form" : userform})
    # elif request.method == "POST":
    #     return postuser(request)


    # people = Person.objects.all()
    # userform = UserForm()
    # return render(request, "index3.html", {"form" : userform, "people" : people})
    return render(request, "index4.html")

# def create(request):
#     if request.method == "POST":
#         userform = UserForm(request.POST)
#         if userform.is_valid():
#             person = Person()
#             person.name = userform.cleaned_data["name"]
#             person.age = userform.cleaned_data["age"]
#             person.save()
#             return HttpResponseRedirect("/")
#         else:
#             return HttpResponseBadRequest("Invalid data")
#     # else:
#     #     index(request)       

# def edit(request, id):
#     try:
#         person = Person.objects.get(id = id)
#         if request.method == "POST":
#             userform = UserForm(request.POST)
#             if userform.is_valid():
#                 person.name = userform.cleaned_data["name"]
#                 person.age = userform.cleaned_data["age"]
#                 person.save()
#                 return HttpResponseRedirect("/")

#         else:
#             userform = UserForm(initial= {"name": person.name, "age": person.age})
#             return render(request, "edit.html", {"form": userform})
#     except Person.DoesNotExist:
#         return HttpResponseNotFound("Person not found")

# def delete(requst, id):
#     try:
#         person = Person.objects.get(id = id)
#         person.delete()
#         return HttpResponseRedirect("/")
#     except Person.DoesNotExist:
#         return HttpResponseNotFound("Person not found")



# def postuser(request):
#     name = request.POST.get("name", "undefined")
#     age = request.POST.get("age", "undefined")
#     return HttpResponse(f"<h2>NAME: {name} <br> AGE: {age}</h2>")

# def products(request):
#     return HttpResponse("Produsts list")

# def product(request, id):
#     return HttpResponse(f"Product №{id}")
 
# def new(request):
#     return HttpResponse("New products")
 
# def top(request):
#     return HttpResponse("Top products")

# def comments(request, id):
#     return HttpResponse(f"Comments about product №{id}")

# def questions(request, id):
#     return HttpResponse(f"Questions about product №{id}")

# def user(request):
#     age = request.GET.get("age", "Undefined")
#     name = request.GET.get("name", "Undefined")
#     return HttpResponse(f"<h2>NAME: {name} <br> AGE: {age}</h2>")