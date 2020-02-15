from django.contrib import admin

from .models import Customer, Job, Technician


admin.site.register(Customer)
admin.site.register(Job)
admin.site.register(Technician)