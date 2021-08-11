from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "HelloShreck/index.html")


def idn(request):
    return render(request, "HelloShreck/Terms of use.html")
