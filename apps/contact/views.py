from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactMessageForm


def contact(request):
    privacy_error = None

    if request.method == "POST":
        form = ContactMessageForm(request.POST)

        privacy_accepted = request.POST.get("privacy")

        if not privacy_accepted:
            privacy_error = "يجب الموافقة على سياسة الخصوصية وشروط الاستخدام."

        elif form.is_valid():
            form.save()
            return redirect("contact:success")

    else:
        form = ContactMessageForm()

    context = {
        "form": form,
        "privacy_error": privacy_error,
    }

    return render(
        request,
        "contact/contact.html",
        context,
    )

def success(request):
    return render(request, "contact/success.html")