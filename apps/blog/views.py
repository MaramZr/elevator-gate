from django.shortcuts import get_object_or_404, render
from .models import BlogCategory, BlogPost

# Create your views here.
def blog_list(request):
    posts = BlogPost.objects.filter(is_published=True).order_by("-published_at")

    context = {
        "posts": posts,
    }

    return render(request, "blog/blog_list.html", context)


def blog_detail(request, slug):
    post = get_object_or_404(
        BlogPost,
        slug=slug,
        is_published=True,
    )

    context = {
        "post": post,
    }

    return render(request, "blog/blog_detail.html", context)