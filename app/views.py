from django.conf import settings
from django.shortcuts import render
from .models import Slider
from types import SimpleNamespace as dummy


def index(request):
    slider_images = list(Slider.objects.all())

    slider_maxlength = 5+1  # для корректной версти клайдера должно быть на одну картинку больше
    # если картинок в слайдере недостает, рендерим в слайдер noimage.jpg
    if len(slider_images) < slider_maxlength:
        noimage_url = f"{settings.MEDIA_URL}noimage.jpg"
        
        count_noimage_in_slider = slider_maxlength-len(slider_images)
        empty_images = [
            dummy(title="noimage", image=dummy(url=noimage_url))
        ]*count_noimage_in_slider


        slider_images += empty_images

    return render(request, "index.html", {"images": slider_images})
