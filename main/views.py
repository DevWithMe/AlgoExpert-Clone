from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def info(request, section):
    if section != "problem":
        return HttpResponse("Hello World")
    return HttpResponse("Hello Problem!")