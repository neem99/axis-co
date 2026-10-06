from django.shortcuts import render
from .models import Testimonial

# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def about(request) :
    return render(request,"about.html")

def testimonials(request) :
    testimonials = Testimonial.objects.filter(is_published=True)

    return render(
        request,
        "testimonials.html",
        {"testimonials" : testimonials}
    )


