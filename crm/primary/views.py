from django.shortcuts import render

from .models import Customer, Job, Technician

def home(request):
    context = {'title' : 'Home'}
    return render(request, 'primary/home.html', context=context)

def jobs(request):
    context = {
        'jobs' : Job.objects.all()
    }
    return render(request, 'primary/jobs.html', context=context)

def job(request):
    context = {}
    return render(request, 'primary/job.html', context=context)

def customers(request):
    context = {
        'customers' : Customer.objects.all()
    }
    return render(request, 'primary/customers.html', context=context)

def customer(request):
    context = {}
    return render(request, 'primary/customer.html', context=context)

def technicians(request):
    context = {
        'technicians' : Technician.objects.all()
    }
    return render(request, 'primary/technicians.html', context=context)

def technician(request):
    context = {}
    return render(request, 'primary/technician.html', context=context)