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

            