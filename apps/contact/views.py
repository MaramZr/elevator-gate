from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactMessageForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "You have new messages has been sent successfully."
            )

            return redirect("contact:contact")  # Redirect to a success page after saving the form
    else:
        form = ContactMessageForm()

    context = {
        "form": form,
    }
    return render(request, 'contact/contact.html', context)
            
            
        