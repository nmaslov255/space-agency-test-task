from django.db import models
from filer.fields.image import FilerImageField

class SliderImage(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = FilerImageField(on_delete=models.CASCADE, related_name="slider_images")
    order = models.PositiveIntegerField(default=0, db_index=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title or f"Image {self.pk}"