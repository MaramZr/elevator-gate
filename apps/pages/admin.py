from django.contrib import admin

# Register your models here.
from .models import Testimonial, FAQ

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "order")
    search_fields = ("name", "message")
    list_filter = ("is_active",)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "is_active", "order")
    search_fields = ("question", "answer")
    list_filter = ("is_active",)