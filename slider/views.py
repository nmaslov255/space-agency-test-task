from django.shortcuts import render
from .models import SliderImage

def index(request):
    images = SliderImage.objects.all()
    return render(request, "index.html", {"images": images})