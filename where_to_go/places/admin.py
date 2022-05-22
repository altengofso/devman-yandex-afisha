from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin
from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ['preview']
    extra = 0

    def preview(self, image):
        return format_html('<img src="{}" height="200"/>', image.image.url)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = ['title']
