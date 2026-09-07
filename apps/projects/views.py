from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
# Create your views here
from .models import Project, ProjectCategory

def project_list(request):
    projects = Project.objects.filter(is_featured=True).order_by('order')

    context = {
        'projects': projects
    }

    return render(request, "projects/project_list.html", context)


def project_detail(request, slug):
    project = get_object_or_404(
        Project,
        slug=slug,
        is_featured=True,
    )

    context = {
        "project": project,
    }

    return render(request, "projects/project_detail.html", context)


