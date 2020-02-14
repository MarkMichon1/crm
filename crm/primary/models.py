from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Customer(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} -- {self.street_address} -- {self.city}'

    def get_absolute_url(self):
        return reverse('primary-customer', kwargs={'pk' : self.pk})


class Technician(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=10, default="0000000000")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} -- {self.is_active}'

    def get_absolute_url(self):
        return reverse('primary-technician', kwargs={'pk' : self.pk})


class Job(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    technicians = models.ManyToManyField(Technician, null=True)
    cost_of_job = models.DecimalField(max_digits=8, decimal_places=2)
    is_complete = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(default=None, null=True)

    def get_absolute_url(self):
        return reverse('primary-job', kwargs={'pk' : self.pk})


class TechnicianComment(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)


class CustomerComment(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)


class JobComment(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
