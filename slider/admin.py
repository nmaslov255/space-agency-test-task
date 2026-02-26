from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SliderImage

@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("title", "order")