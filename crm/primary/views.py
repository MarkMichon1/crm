from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Customer, Job, Technician
from .utilities import reset_app_sample_state

def home(request):
    context = {'title' : 'Home'}
    return render(request, 'primary/home.html', context=context)

@login_required
def jobs(request):
    context = {
        'jobs' : Job.objects.all(),
        'title' : 'Jobs'
    }
    return render(request, 'primary/jobs.html', context=context)

@login_required
def job(request):
    context = {}
    return render(request, 'primary/job.html', context=context)


class CustomerListView(LoginRequiredMixin, ListView): #todo turn back into function
    model = Customer
    template_name = 'primary/customers.html'
    context_object_name = 'customers'
    extra_context = {
        'title': 'Customers'
    }
    ordering = ['last_name', 'first_name'] #todo check


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'primary/customer.html'
    extra_context = {
        'title': 'Customer Information'
    }


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    template_name = 'primary/customer_create.html'
    fields = ['first_name', 'last_name', 'street_address', 'city', 'state', 'zip_code', 'phone_number']
    extra_context = {
        'title': 'Add New Customer'
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    template_name = 'primary/customer_create.html'
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

@login_required
def customer(request):
    context = {}
    return render(request, 'primary/customer.html', context=context)

@login_required
def technicians(request):
    context = {
        'technicians' : Technician.objects.all(),
        'title': 'Technicians'
    }
    return render(request, 'primary/technicians.html', context=context)

@login_required
def technician(request):
    context = {}
    return render(request, 'primary/technician.html', context=context)

def reset_state(request):
    reset_app_sample_state()
    messages.success(request, 'Application state successfully reset!')
    return redirect('primary-home')