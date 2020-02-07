from django.urls import path
from . import views

urlpatterns = [
    path('customer', views.customer, name='primary-customer'),
    path('customers', views.customers, name='primary-customers'),
    path('job', views.job, name='primary-job'),
    path('jobs', views.jobs, name='primary-jobs'),
    path('technician', views.technician, name='primary-technician'),
    path('technicians', views.technicians, name='primary-technicians'),
    path('', views.home, name='primary-home'),
]