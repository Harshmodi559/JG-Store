from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','name','date']

admin.site.register(Customer,CustomerAdmin)