from django.shortcuts import render

def home(request):
    context = {'title' : 'Home'}
    return render(request, 'primary/home.html', context=context)

def jobs(request):
    context = {}
    return render(request, 'primary/jobs.html', context=context)

def job(request):
    context = {}
    return render(request, 'primary/job.html', context=context)

def customers(request):
    context = {}
    return render(request, 'primary/customers.html', context=context)

def customer(request):
    context = {}
    return render(request, 'primary/customer.html', context=context)

def technicians(request):
    context = {}
    return render(request, 'primary/technicians.html', context=context)

def technician(request):
    context = {}
    return render(request, 'primary/technician.html', context=context)