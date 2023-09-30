from django.shortcuts import render
from .forms import ApplicationForm
from .models import DbForm
from django.contrib import messages
from django.core.mail import EmailMessage


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            DbForm.objects.create(first_name=first_name,
                                  last_name=last_name,
                                  email=email, date=date,
                                  occupation=occupation)

            message_body = f"A new job application was submitted, Thank you {first_name} {last_name}"
            email_message = EmailMessage("Application Confirmation", message_body, to=[email])
            email_message.send()

            messages.success(request, "Form Submitted Successfully, We will reach out!")

    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")
