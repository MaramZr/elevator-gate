from django.shortcuts import get_object_or_404, render
from .models import BlogCategory, BlogPost
from django.db.models import Q
from django.core.paginator import Paginator

app_name = "blog"  

# Create your views here.
def blog_list(request):

    published_posts = (
        BlogPost.objects
        .filter(is_published=True)
        .select_related("category", "author")
        .order_by("-published_at", "-created_at")
    )

    # Latest published article in the featured section
    featured_post = published_posts.first()

    # All published articles in the regular listing
    posts = published_posts

    # Active categories
    categories = (
        BlogCategory.objects
        .filter(is_active=True)
        .order_by("order", "name")
    )

    search_query = request.GET.get("q", "").strip()
    active_category = request.GET.get("category", "").strip()

    # Search by title, excerpt or content
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query)
            | Q(excerpt__icontains=search_query)
            | Q(content__icontains=search_query)
        )

    # Filter by category
    if active_category:
        posts = posts.filter(
            category__slug=active_category,
            category__is_active=True
        )

    # Pagination
    paginator = Paginator(posts, 6)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = {
        "featured_post": featured_post,
        "posts": posts,
        "categories": categories,
        "search_query": search_query,
        "active_category": active_category,
        "page_obj": page_obj,
        "paginator": paginator,
        "is_paginated": paginator.num_pages > 1,
    }
    return render(request, "blog/blog_list.html", context)

def blog_detail(request, slug):
    post = get_object_or_404(
        BlogPost.objects.select_related("category", "author"),
        slug=slug,
        is_published=True,
    )

    # Reading time based on article content
    word_count = len(post.content.split())
    reading_time = max(1, round(word_count / 200))

    published_posts = (
        BlogPost.objects
        .filter(is_published=True)
        .select_related("category", "author")
        .order_by("-published_at", "-created_at")
    )



    related_posts = (
        BlogPost.objects
        .filter(
            is_published=True,
            category=post.category,
        )
        .exclude(pk=post.pk)
        .select_related("category")
        .order_by("-published_at", "-created_at")[:3]
    )

    context = {
        "post": post,
        "reading_time": reading_time,
        "related_posts": related_posts,
    }
    return render(request, "blog/blog_detail.html", context)