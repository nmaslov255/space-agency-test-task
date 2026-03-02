from django.shortcuts import render
from slider.models import SliderImage

def index(request):
    images = SliderImage.objects.all()
    return render(request, "index.html", {"images": images})
