from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Brick)
class BrickAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image")

    def brick_id(self, obj):
        return obj.id

    def brick_name(self, obj):
        return obj.name

    def brick_image(self, obj):
        return obj.image

    brick_id.short_description = "ID"
    brick_name.short_description = "Name"
    brick_image.short_description = "Image"


@admin.register(Manual)
class ManualAdmin(admin.ModelAdmin):
    list_display = ("id", "name", 'number_of_pages', "image")

    def manual_id(self, obj):
        return obj.id

    def manual_name(self, obj):
        return obj.name

    def manual_number_of_pages(self, obj):
        return obj.number_of_pages

    def manual_image(self, obj):
        return obj.image

    manual_id.short_description = "ID"
    manual_name.short_description = "Name"
    manual_number_of_pages.short_description = "Number of pages"
    manual_image.short_description = "Image"


@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    list_display = ("id", "name", 'year', 'price', "image")

    def set_id(self, obj):
        return obj.id

    def set_name(self, obj):
        return obj.name

    def set_year(self, obj):
        return obj.year

    def set_price(self, obj):
        return obj.price

    def set_image(self, obj):
        return obj.image

    set_id.short_description = "ID"
    set_name.short_description = "Name"
    set_year.short_description = "Release year"
    set_price.short_description = "Price in USD($)"
    set_image.short_description = "Image"
