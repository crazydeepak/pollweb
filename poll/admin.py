from django.contrib import admin

# Register your models here.
from .models import Monitor, Response
admin.site.register(Monitor)
admin.site.register(Response)
