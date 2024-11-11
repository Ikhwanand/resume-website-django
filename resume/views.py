from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import Contact

# Create your views here.
def home(request):
    return render(request, 'resume/home.html')


def resume(request):
    return render(request, 'resume/resume.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            contact = form.save()

            # Process the form data (e.g., send an email)
            send_mail(
                'Contact Form Submission',
                f'Name: {contact.name}\nEmail: {contact.email}\nPhone: {contact.phone}\nMessage: {contact.message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )

            # Redirect to the success page
            return redirect('resume:success')
    else:
        form = ContactForm()

    return render(request, 'resume/contact.html', {'form': form})

def success_view(request):
    return render(request, 'resume/success.html')

def projects(request):
    return render(request, 'resume/projects.html')