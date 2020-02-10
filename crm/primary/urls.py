from django.urls import path
from .views import CustomerListView
from . import views

urlpatterns = [
    path('customer', views.customer, name='primary-customer'),
    path('customers', CustomerListView.as_view(), name='primary-customers'),
    path('job', views.job, name='primary-job'),
    path('jobs', views.jobs, name='primary-jobs'),
    path('reset-state', views.reset_state, name='primary-reset-state'),
    path('technician', views.technician, name='primary-technician'),
    path('technicians', views.technicians, name='primary-technicians'),
    path('', views.home, name='primary-home'),
]