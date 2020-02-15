from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Customer, Job, Technician
from .utilities import reset_app_sample_state

def home(request):
    pending_jobs = Job.objects.filter(is_complete=False).count()
    completed_jobs = Job.objects.filter(is_complete=True).count()
    total_customers = Customer.objects.count()
    employed_technicians = Technician.objects.filter(is_active=True).count()
    context = {'title' : 'Home',
               'pending_jobs' : pending_jobs,
               'completed_jobs' : completed_jobs,
               'total_customers' : total_customers,
               'employed_technicians' : employed_technicians
               }
    return render(request, 'primary/home.html', context=context)


class JobListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'primary/jobs.html'
    context_object_name = 'jobs'
    extra_context = {
        'title': 'Jobs'
    }
    paginate_by = 10


class JobDetailView(LoginRequiredMixin, DetailView):
    model = Job
    template_name = 'primary/job.html'
    extra_context = {
        'title': 'Job Information'
    }


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    template_name = 'primary/object_create_update.html'
    fields = ['customer', 'cost_of_job', 'technicians', 'job_details']
    extra_context = {
        'title': 'Add New Job'
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    template_name = 'primary/object_create_update.html'
    fields = ['customer', 'cost_of_job', 'technicians', 'is_complete', 'date_completed', 'job_details']
    extra_context = {
        'title': 'Update Job Information'
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class JobDeleteView(LoginRequiredMixin, DeleteView):
    model = Job
    template_name = 'primary/job_delete.html'
    success_url = '/jobs'
    extra_context = {
        'title': 'Remove Job?'
    }


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'primary/customers.html'
    context_object_name = 'customers'
    extra_context = {
        'title': 'Customers'
    }
    ordering = ['last_name', 'first_name'] #todo check
    paginate_by = 10


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'primary/customer.html'
    extra_context = {
        'title': 'Customer Information'
    }


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    template_name = 'primary/object_create_update.html'
    fields = ['first_name', 'last_name', 'street_address', 'city', 'state', 'zip_code', 'phone_number']
    extra_context = {
        'title': 'Add New Customer'
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    template_name = 'primary/object_create_update.html'
    fields = ['first_name', 'last_name', 'street_address', 'city', 'state', 'zip_code', 'phone_number']
    extra_context = {
        'title': 'Update Customer Information'
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'primary/customer_delete.html'
    success_url = '/customers'
    extra_context = {
        'title': 'Remove Customer?'
    }


class TechnicianListView(LoginRequiredMixin, ListView):
    model = Technician
    template_name = 'primary/technicians.html'
    context_object_name = 'technicians'
    extra_context = {
        'title': 'Technicians'
    }
    ordering = ['last_name', 'first_name']
    paginate_by = 10


class TechnicianDetailView(LoginRequiredMixin, DetailView):
    model = Technician
    template_name = 'primary/technician.html'
    extra_context = {
        'title': 'Technician Information'
    }


class TechnicianCreateView(LoginRequiredMixin, CreateView):
    model = Technician
    template_name = 'primary/object_create_update.html'
    fields = ['first_name', 'last_name', 'street_address', 'city', 'state', 'zip_code', 'email', 'phone_number']
    extra_context = {
        'title': 'Add New Technician'
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TechnicianUpdateView(LoginRequiredMixin, UpdateView):
    model = Technician
    template_name = 'primary/object_create_update.html'
    fields = ['first_name', 'last_name', 'street_address', 'city', 'state', 'zip_code', 'email', 'phone_number',
              'is_active']
    extra_context = {
        'title': 'Update Technician Information'
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TechnicianDeleteView(LoginRequiredMixin, DeleteView):
    model = Technician
    template_name = 'primary/technician_delete.html'
    success_url = '/technicians'
    extra_context = {
        'title': 'Remove Technician?'
    }


def reset_state(request):
    reset_app_sample_state()
    messages.success(request, 'Application state successfully reset!')
    return redirect('primary-home')