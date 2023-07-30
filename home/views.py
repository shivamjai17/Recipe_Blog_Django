from django.shortcuts import render

# Create your views here.
from django.http import request


def home(response):
    people=['Shiv','naru','geet']
    return render(response ,"index.html",context={'people':people})


def about(response):
    people=['Shiv','naru','geet']
    return render(response ,"about.html")