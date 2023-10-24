from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to emobilis")


def about(request):
    return HttpResponse("About emobilis")


def contact(request):
    return HttpResponse("Contact Emobilis")
