from django.contrib import admin

from .models import Customer, CustomerComment, Job, JobComment, Technician, TechnicianComment


admin.site.register(Customer)
admin.site.register(CustomerComment)
admin.site.register(Job)
admin.site.register(JobComment)
admin.site.register(Technician)
admin.site.register(TechnicianComment)