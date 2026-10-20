from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from apps.services.models import Service
from apps.projects.models import Project
from apps.blog.models import BlogPost



class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "monthly"
    # اشارات لمحركات البحث عن اهمية الصحفات و معدل تغيرها،وليست أوامر تضمن أن Google سيزور الصفحة شهريًا

    def items(self):
        return [
            "pages:home",
            "pages:about",
            "services:service_list",
            "projects:project_list",
            "blog:blog_list",
            "pages:faq",
            "contact:contact",
        ]

    def location(self, item):
        return reverse(item)


class ServiceSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return Service.objects.filter(is_active=True)

    def location(self, obj):
        return reverse(
            "services:service_detail",
            kwargs={"slug": obj.slug},
        )


class ProjectSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Project.objects.all()

    def location(self, obj):
        return reverse(
            "projects:project_detail",
            kwargs={"slug": obj.slug},
        )


class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return BlogPost.objects.filter(is_published=True)

    def location(self, obj):
        return reverse(
            "blog:blog_detail",
            kwargs={"slug": obj.slug},
        )