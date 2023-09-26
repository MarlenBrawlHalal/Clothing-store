from django.contrib import admin
from .models import Clothes, Review

class ReviewInline(admin.TabularInline):
    model = Review

class ClothesAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]

admin.site.register(Clothes, ClothesAdmin)