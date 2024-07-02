from django.shortcuts import render
from .models import NavbarItem, AboutUs, Service

def index(request):
    navbar_items = NavbarItem.objects.all()
    return render (request, 'center/index.html', {'navbar_items': navbar_items})

def about_us(request):
    navbar_items = NavbarItem.objects.all()
    about_us_content = AboutUs.objects.first()
    return render(request, 'center/about_us.html', {'navbar_items': navbar_items, 'about_us_content': about_us_content})

def service(request):
    navbar_items = NavbarItem.objects.all()
    service = Service.objects.all()
    return render(request, 'center/service.html', {'navbar_items': navbar_items, 'service': service})

