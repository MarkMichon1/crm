from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import ListView

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


# @login_required todo
class CustomerListView(ListView):
    model = Customer
    template_name = 'primary/customers.html'
    context_object_name = 'customers'
    extra_context = {
        'title': 'Customers'
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