from django.contrib import admin

from .models import Company, Events

admin.site.register(Company)
admin.site.register(Events)