from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
# Create your views here
from .models import Project, ProjectCategory    
from django.core.paginator import Paginator

def project_list(request):
    projects = (
        Project.objects
        .select_related("category", "service")
        .order_by("order", "-created_at")
        )

    categories = ProjectCategory.objects.filter(is_active=True).order_by("order", "name")

    category_slug = request.GET.get("category")

    if category_slug:
        projects = projects.filter(category__slug=category_slug)

    paginator = Paginator(projects, 6)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = {
        "projects": page_obj,
        "page_obj": page_obj,
        "paginator": paginator,
        "is_paginated": paginator.num_pages > 1,
        "categories": categories,
        "active_category": category_slug,
    }

    return render(request, "projects/project_list.html", context)


def project_detail(request, slug):
    project = get_object_or_404(
        Project.objects.select_related("category", "service"),
        slug=slug
    )

    related_projects = (
        Project.objects
        .select_related("category", "service")
        .exclude(pk=project.pk)
        .order_by("order", "-created_at")[:3]
    )

    context = {
        "project": project,
        "related_projects": related_projects,
    }

    return render(request, "projects/project_detail.html", context)

