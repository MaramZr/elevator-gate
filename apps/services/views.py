from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Service

def service_list(request):
    services = Service.objects.filter(is_active=True).order_by('order')

    context = {
        'services': services
    }

    return render(request, "services/service_list.html", context)

def service_detail(request, slug):
    service = get_object_or_404(
        Service,
        slug=slug,# الاولى هي اسم الفيلد المموجود داخل المودل والتانية هي قيمة المتغير الي واصلة على الفيو من الباث
        is_active=True,
    )

    other_services = (
        Service.objects
        .filter(is_active=True)
        .exclude(pk=service.pk)
        .order_by("order")[:3]
    )

    context = {
        "service": service,
        "other_services": other_services,
    }

    return render(request, "services/service_detail.html", context)