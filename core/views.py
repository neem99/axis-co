from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def about(request) :
    return render(request,"about.html")

def testimonials(request) :
    return render(request, "testimonials.html")


