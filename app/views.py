from django.conf import settings
from django.shortcuts import render
from .models import Slider


def index(request):
    slider_images = Slider.objects.all()

    return render(request, "index.html", {"images": slider_images})
