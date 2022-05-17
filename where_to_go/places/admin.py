from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['preview']
    fields = ['image', 'preview', 'order']

    def preview(self, image):
        return format_html('<img src="{}" height="200"/>', image.image.url)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     readonly_fields = ['preview']
#
#     def preview(self, image):
#         return format_html('<img src="{}" height="200"/>', image.image.url)
