from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Customer(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date_added = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=10)

    @property
    def lifetime_value(self):
        job_total = 0
        for job in self.jobs.all():
            job_total += job.cost_of_job
        return job_total
    def __str__(self):
        return f'{self.first_name} {self.last_name} -- {self.street_address} -- {self.city}'

    def get_absolute_url(self):
        return reverse('primary-customer', kwargs={'pk' : self.pk})

    class Meta:
        ordering = ('last_name', 'first_name')


class Technician(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date_added = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        if self.is_active:
            active_status = 'Employed'
        else:
            active_status = 'INACTIVE'
        return f'{self.first_name} {self.last_name} -- {active_status}'

    def get_absolute_url(self):
        return reverse('primary-technician', kwargs={'pk' : self.pk})

    class Meta:
        ordering = ('last_name', 'first_name')


class Job(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(to=Customer, related_name='jobs', null=True, on_delete=models.SET_NULL)
    technicians = models.ManyToManyField(to=Technician, related_name='jobs', blank=True)
    cost_of_job = models.DecimalField(max_digits=8, decimal_places=2)
    is_complete = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(default=None, null=True, blank=True)
    job_details = models.TextField(null=True)

    def get_absolute_url(self):
        return reverse('primary-job', kwargs={'pk' : self.pk})

    class Meta:
        ordering = ('-date_added',)