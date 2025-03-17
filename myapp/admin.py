from django.utils.html import format_html
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock','image_tag')  # Customize displayed columns
    search_fields = ('name',)  # Add search functionality
    list_filter = ('price',)  # Add filter options

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:5px;"/>'.format(obj.image.url))
        return "(No Image)"

    image_tag.short_description = "Image"
admin.site.register(Product, ProductAdmin)

