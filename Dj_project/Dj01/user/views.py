from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def username(rend):
    return HttpResponse("<h2>Hello World,你哈</h2>")
