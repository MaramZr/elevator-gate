from django.contrib import admin

# Register your models here.
from .models import Project, ProjectCategory

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_featured", "order")
    list_filter = ("category", "is_featured")
    search_fields = ("title", "short_description")
    prepopulated_fields = {"slug": ("title",)}