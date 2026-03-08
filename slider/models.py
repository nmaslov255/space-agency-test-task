from django.db import models
from filer.fields.image import FilerImageField

class SliderImage(models.Model):
    title = models.CharField(max_length=255, blank=True, verbose_name="Заголовок")
    image = FilerImageField(on_delete=models.CASCADE, related_name="slider_images", verbose_name="Изображения")
    order = models.PositiveIntegerField(default=0, db_index=True, verbose_name="Порядок")

    class Meta:
        ordering = ["order"]
        verbose_name = "Слайдер"
        verbose_name_plural = "Слайды"

    def __str__(self):
        return self.title or f"Image {self.pk}"