# Django_project3typemodels__1-1__1-M__M-M

Django_project3typemodels__1-1__1-M__M-M

D:\pydjango\tareas-test

django-admin startproject project3typemodels

..o\tareas-test\project3typemodels

[manage.py]

python manage.py startapp typemodels3


..\tareas-test\project3typemodels\project3typemodels

  settings.py 
  
INSTALLED_APPS = [

    #...,
    
    'typemodels3',
    
]


> modelos

  ..\tareas-test\project3typemodels\typemodels3
  
  models.py
  
  # add code..
  
  # ...code at final...

..\tareas-test\project3typemodels

[manage.py]

manage.py makemigrations

manage.py migrate

> Activar modelos en el Admin de Django

 ..\tareas-test\project3typemodels\typemodels3
 
 admin.py 
 
 # add code..

user:

python manage.py createsuperuser

Ej. (user,key) : ...

python manage.py runserver

  http://127.0.0.1:8000/

administration panel :

http://localhost:8000/admin/


> models.py

from django.db import models

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
    
    
> admin.py

from django.contrib import admin

# Register your models here.

from . import models 

@admin.register(models.Vendor)

class VendorAdmin(admin.ModelAdmin):

    list_display = ('name',)
    
    search_fields = ('name',)
    
@admin.register(models.License)   

class LicenseAdmin(admin.ModelAdmin):

    list_display = ('name', 'vendor',)
    
    search_fields = ('name',)


@admin.register(models.Customer)   

class CustomerAdmin(admin.ModelAdmin):

    list_display = ('name',)
    
    search_fields = ('name',)

@admin.register(models.Vehicle)   

class VehicleAdmin(admin.ModelAdmin):

    list_display = ('name', 'customer',)
    
    search_fields = ('name',)

    
@admin.register(models.Worker)      

class WorkerAdmin(admin.ModelAdmin):

    list_display = ('name',)
    
    search_fields = ('name',)

@admin.register(models.Machine)     

class MachineAdmin(admin.ModelAdmin):

    #list_display = ('name', 'worker',)
    
    list_display = ('name','get_workers')
    
    search_fields = ('name',)
    
    def get_workers(self, obj):
    
            return "\n".join([p.name for p in obj.worker.all()])



M-M

@admin.register(models.Machine)  

class MachineAdmin(admin.ModelAdmin):

    #list_display = ('name', 'worker',)
    
    list_display = ('name','get_workers')
    
    search_fields = ('name',)
    
    def get_workers(self, obj):
    
            return "\n".join([p.name for p in obj.worker.all()])
