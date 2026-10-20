from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def robots_txt(request):
    content = """User-agent: *
                Disallow: /admin/
                Sitemap: /sitemap.xml
            """
    return HttpResponse(content, content_type="text/plain")