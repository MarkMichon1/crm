from django.urls import path
from .views import CustomerCreateView, CustomerDeleteView, CustomerDetailView, CustomerListView, CustomerUpdateView
from . import views

urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='primary-customers'),
    path('customer/new/', CustomerCreateView.as_view(), name='primary-customer-create'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='primary-customer'),
    path('customer/<int:pk>/update/', CustomerUpdateView.as_view(), name='primary-customer-update'),
    path('customer/<int:pk>/delete/', CustomerDeleteView.as_view(), name='primary-customer-delete'),
    path('job/', views.job, name='primary-job'),
    path('jobs/', views.jobs, name='primary-jobs'),
    path('reset-state/', views.reset_state, name='primary-reset-state'),
    path('technician/', views.technician, name='primary-technician'),
    path('technicians/', views.technicians, name='primary-technicians'),
    path('', views.home, name='primary-home'),
]