from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Lead


# Create booking view
def book(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip()

        if not full_name or not email:
            return render(request, "booking/book.html", {
                "error": "Please fill in both fields."
            })

        Lead.objects.create(full_name=full_name, email=email)

        send_mail(
            subject="Thanks for reaching out",
            message=(
                f"Hi {full_name},\n\n"
                f"We received your inquiry.\n"
                f"Here is the information you submitted:\n"
                f"Name: {full_name}\n"
                f"Email: {email}\n\n"
                f"We will be in touch soon."
            ),
            # Temporary email setup, TODO create an email backend to handle email sending
            from_email="hello@weddingapp.com",
            recipient_list=[email],
            fail_silently=False,
        )

        return redirect("book_thanks")

    return render(request, "booking/book.html")


def book_thanks(request):
    return render(request, "booking/thanks.html")
