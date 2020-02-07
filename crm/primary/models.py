from django.contrib.auth.models import AbstractUser
from django.db import models


# class User(AbstractUser):
#     email = models.EmailField(verbose_name='email', max_length=255, unique=True)
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
#     USERNAME_FIELD = 'email'
#
#     def get_username(self):
#         return self.email


class Customer(models.Model):
    name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=10, default="0000000000")

    def __str__(self):
        return f'{self.name} -- {self.street_address} -- {self.city}'


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