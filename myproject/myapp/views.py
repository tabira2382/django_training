from django.shortcuts import render
from django.http import HttpResponse


def Index(reqest):
    return HttpResponse ("Hello World")
