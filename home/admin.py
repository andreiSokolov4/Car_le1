from django.contrib import admin
from .models import Car, Photo

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

class CarAdmin(admin.ModelAdmin):
    list_display = ('mark', 'model', 'price', 'miles', 'year', 'fuel_type', 'transmission', 'drive_type', 'condition', 'engine_size', 'doors', 'cylinders', 'color', 'vin')
    search_fields = ('mark', 'model', 'vin')
    list_filter = ('fuel_type', 'transmission', 'drive_type', 'condition', 'year')
    inlines = [PhotoInline]

admin.site.register(Car, CarAdmin)
admin.site.register(Photo)
