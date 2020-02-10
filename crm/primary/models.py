from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
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


class Technician(models.Model):
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


class Job(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    technicians = models.ManyToManyField(Technician, null=True)
    is_complete = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(default=None, null=True)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
