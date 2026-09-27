from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactMessageForm


def contact(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "تم استلام طلبك بنجاح."
            )

            return redirect("contact:success")

    else:
        form = ContactMessageForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "contact/contact.html",
        context,
    )

def success(request):
    return render(request, "contact/success.html")