from django.contrib import admin
from .models import ServiceRequest, Society, Resident
# Register your models here.
admin.site.register(Society)
admin.site.register(ServiceRequest)
admin.site.register(Resident)
