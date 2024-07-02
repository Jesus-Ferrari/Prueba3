from django.contrib import admin
from .models import NavbarItem,AboutUs, Service

# Register your models here.
admin.site.register(NavbarItem)
admin.site.register(AboutUs)
admin.site.register(Service)