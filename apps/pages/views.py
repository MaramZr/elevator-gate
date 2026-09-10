from django.shortcuts import render
from apps.blog.models import BlogPost
from apps.services.models import Service
from apps.projects.models import Project

from .models import FAQ, Testimonial


def home(request):
    blog_posts = BlogPost.objects.filter(is_published=True).order_by("created_at")[:3]
    projects = Project.objects.filter(is_featured=True).order_by("created_at")[:3]
    services = Service.objects.filter(is_active=True).order_by("order")[:3]
    testimonials = Testimonial.objects.filter(is_active=True).order_by("order")
    faqs = FAQ.objects.filter(is_active=True).order_by("order")

    context = {
        "blog_posts": blog_posts,
        "projects": projects,
        "services": services,
        "testimonials": testimonials,
        "faqs": faqs,
    }

    return render(request, "pages/home.html", context)

def about(request):
    return render(request, "pages/about.html")

def testimonials(request):
    testimonials = Testimonial.objects.filter(is_active=True).order_by("order")
    context = {
        "testimonials": testimonials,
    }
    return render(request, "pages/testimonials.html", context)

def faq(request):
    faqs = FAQ.objects.filter(is_active=True).order_by("order")
    context = {
        "faqs": faqs,
    }
    return render(request, "pages/faq.html", context)