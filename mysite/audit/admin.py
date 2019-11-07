from django.contrib import admin

from .models import Lead, Person, Organization

# Register your models here.
admin.site.register(Lead)
admin.site.register(Person)
admin.site.register(Organization)
