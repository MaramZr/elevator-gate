from django.contrib import admin

# Register your models here.
from .models import Service, ServiceFeature

class ServiceFeatureInline(admin.TabularInline):# يعني أننا نريد عرض ServiceFeature كصفوف صغيرة داخل صفحة Service.

    model = ServiceFeature # يعني اي مودل مرتبط نريد عرضه
    extra = 1 #فتعني أن ديجانجو سيعرض صفًا فارغًا واحدًا جاهزًا لإضافة فيتشر جديدة

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_active", "order")
    list_filter = ("is_active",)
    search_fields = ("title", "short_description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ServiceFeatureInline]


@admin.register(ServiceFeature)
class ServiceFeatureAdmin(admin.ModelAdmin):
    list_display = ("title", "service", "order")
    list_filter = ("service",)
    search_fields = ("title", "description")