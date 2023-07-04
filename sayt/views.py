from django.shortcuts import render

from sayt.models import Contact, Subscribe


# Create your views here.


def index(requests):
    ctx = {}
    if requests.POST:
        email = requests.POST.get('email')
        Subscribe.objects.create(
            email=email
        )
        ctx = {
            "email": email
        }
    return render(requests, "index.html", ctx)

def contact(requests):
    ctx = {}
    if requests.POST:
        name = requests.POST.get('name')
        message = requests.POST.get('message')
        phone = requests.POST.get('phone')
        email = requests.POST.get('email')
        Contact.objects.create(
            name=name, message=message, phone=phone, email=email
        )

        ctx = {
            "contact": contact,

        }
    return render(requests, "contact.html", ctx)

def service(requests):
    ctx = {}
    if requests.POST:
        email = requests.POST.get('email')
        Subscribe.objects.create(
            email=email
        )
        ctx = {
            "email": email
        }
    return render(requests, "service.html", ctx)

def about(requests):
    ctx = {}
    if requests.POST:
        email = requests.POST.get('email')
        Subscribe.objects.create(
            email=email
        )
        ctx = {
            "email": email
        }
    return render(requests, "about.html", ctx)