from django.conf import settings
from django.shortcuts import render
from .models import Slider
from types import SimpleNamespace as SN

def index(request):
    images = list(Slider.objects.all())

    # для корректной версти клайдера должно быть > 5 картинок
    if len(images) < 6:
        delta = 6 - len(images)
        images += [SN(title="noimage", image=SN(url=f"{settings.MEDIA_URL}noimage.jpg"))]*delta

    return render(request, "index.html", {"images": images})
