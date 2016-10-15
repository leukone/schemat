from django.contrib import admin
from .models import Project, Info, ContactInfo

admin.site.register(Project)
admin.site.register(ContactInfo)
admin.site.register(Info)