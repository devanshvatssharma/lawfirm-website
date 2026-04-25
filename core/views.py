from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            # Save to DB
            Contact.objects.create(
                name=name,
                email=email,
                case=message
            )

            # Send Email
            
            send_mail(
                subject=f"New Contact Form Message from {name}",
                message=f"Name: {name}\nEmail: {email}\nMessage:\n{message}",
                from_email=None,
                recipient_list=['devanshvatssharma@gmail.com'],  
            )

            messages.success(request, "Message sent successfully!")
        else:
            messages.error(request, "Please fill all fields")

        return redirect('/#contact')

    return render(request, 'core/home.html')