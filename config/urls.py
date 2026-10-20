"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
from apps.core.sitemaps import StaticViewSitemap, ServiceSitemap , ProjectSitemap, BlogPostSitemap
from apps.core.views import robots_txt

sitemaps ={
    "static": StaticViewSitemap,
    "services": ServiceSitemap,
    "projects": ProjectSitemap,
    "blog": BlogPostSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),


    path('services/', include('apps.services.urls')),
    path('projects/', include('apps.projects.urls')),
    path('blog/', include('apps.blog.urls')),
    path('contact/', include('apps.contact.urls')),
    path('', include('apps.pages.urls')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
        )
    
