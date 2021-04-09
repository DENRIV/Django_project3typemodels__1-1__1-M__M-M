from django.db import models

# Create your models here.

# A) 1-1
class Vendor(models.Model):
    name = models.CharField(max_length=255)
class License(models.Model):
    name = models.CharField(max_length=255)
    vendor = models.OneToOneField(
        Vendor,
        on_delete=models.CASCADE,
        related_name='License'
    )
    
# B) 1-M
class Customer(models.Model):
    name = models.CharField(max_length=255)
class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='Vehicle'
    )

# C) M-M    
class Worker(models.Model):
    name = models.CharField(max_length=255)
class Machine(models.Model):
    name = models.CharField(max_length=255)
    worker = models.ManyToManyField(
        Worker,
        related_name='Machine'
    )    