from django.contrib import admin
from .models import Car, Driver, Trip

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model_name', 'year')

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'date_of_birth')

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('id', 'driver_id', 'car_id', 'distance')

