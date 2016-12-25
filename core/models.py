from django.db import models


# Create your models here.

class Request(models.Model):
    company_name = models.CharField(max_length=128)
    contact_person = models.CharField(max_length=128)
    contact_email = models.EmailField(max_length=128, blank=True)
    contact_number = models.IntegerField()
    budget = models.IntegerField()
    duration = models.IntegerField()
    need_design = models.BooleanField(blank=True)


class Register(models.Model):
    name = models.CharField(max_length=128)
    contact_number = models.IntegerField()
    car_model = models.CharField(max_length=128, blank=True)
    choice = ((0, 'Commercial'), (1, 'Private'))
    commercial_or_private = models.IntegerField(choices=choice)
