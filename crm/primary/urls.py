from django.urls import path
from .views import CustomerCreateView, CustomerDeleteView, CustomerDetailView, CustomerListView, CustomerUpdateView,\
    JobCreateView, JobDeleteView, JobDetailView, JobListView, JobUpdateView, TechnicianCreateView,\
    TechnicianDeleteView, TechnicianDetailView, TechnicianListView, TechnicianUpdateView
from . import views

urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='primary-customers'),
    path('customer/new/', CustomerCreateView.as_view(), name='primary-customer-create'),
    path('customer/<int:pk>/', CustomerDetailView.as_view(), name='primary-customer'),
    path('customer/<int:pk>/update/', CustomerUpdateView.as_view(), name='primary-customer-update'),
    path('customer/<int:pk>/delete/', CustomerDeleteView.as_view(), name='primary-customer-delete'),
    path('jobs/', JobListView.as_view(), name='primary-jobs'),
    path('job/new/', JobCreateView.as_view(), name='primary-job-create'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='primary-job'),
    path('job/<int:pk>/update/', JobUpdateView.as_view(), name='primary-job-update'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='primary-job-delete'),
    path('technicians/', TechnicianListView.as_view(), name='primary-technicians'),
    path('technician/new/', TechnicianCreateView.as_view(), name='primary-technician-create'),
    path('technician/<int:pk>/', TechnicianDetailView.as_view(), name='primary-technician'),
    path('technician/<int:pk>/update/', TechnicianUpdateView.as_view(), name='primary-technician-update'),
    path('technician/<int:pk>/delete/', TechnicianDeleteView.as_view(), name='primary-technician-delete'),
    path('reset-state/', views.reset_state, name='primary-reset-state'),
    path('', views.home, name='primary-home')
]