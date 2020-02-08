from django.contrib import admin

from .models import Comment, Customer, Job, Technician

admin.site.register(Comment)
admin.site.register(Customer)
admin.site.register(Job)
admin.site.register(Technician)