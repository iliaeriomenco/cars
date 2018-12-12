from django.contrib import admin

# Register your models here.

from .models import Car, Driver

class CarAdmin(admin.ModelAdmin):
	list_display = ('id', 'number', 'driver')


admin.site.register(Car, CarAdmin)
admin.site.register(Driver)