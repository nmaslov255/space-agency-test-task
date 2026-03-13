from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin
from .models import Slider


@admin.register(Slider)
class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('preview', 'title', 'order')
    
    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="60"/>', obj.image.url)
        return '—'
    
    preview.short_description = 'Фото'
