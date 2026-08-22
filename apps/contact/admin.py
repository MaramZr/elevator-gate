from django.contrib import admin

# Register your models here.
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "service",
        "subject",
        "is_read",
        "created_at",
    )

    list_filter = ("is_read", "service")

    search_fields = (
        "name",
        "email",
        "phone",
        "subject",
        "message",
    )

    readonly_fields = (
        "name",
        "email",
        "phone",
        "service",
        "subject",
        "message",
        "created_at",
    )

    def has_add_permission(self, request):
        return False