from django.shortcuts import render, get_object_or_404
from .models import Car, Driver, Trip
from django.db.models import Avg
from django.http import JsonResponse

# TODO: при добавлении поездки - добавлять пробег машине участнику
def index(request): #Главная страница
    cars = Car.objects.all() 

    total_cars = Car.objects.count() # Общее количество автомобилей
    total_drivers = Driver.objects.count() 
    total_trips = Trip.objects.count()

    average_mileage = Car.objects.aggregate(avg_mileage = Avg('mileage'))

    context = {
        # 'context' : 'Имя',
        # 'date': datetime.now(),
        'total_cars': total_cars,
        'total_drivers': total_drivers,
        'total_trips': total_trips,
        'average_mileage': average_mileage['avg_mileage'],
        'cars' : cars,
    }
    return render(request, "index.html", context)

def car_detail(request, slug):
    car = get_object_or_404(Car, slug = slug)
    context = {
        'car': car,
    }
    return render(request, 'car_detail.html', context)

def driver_detail(request, slug):
    driver = get_object_or_404(Driver, slug = slug)
    trip_count = driver.trip_as_driver.count()
    context = {
        'driver': driver,
        'trip_count': trip_count,
    }
    return render(request, 'driver_detail.html', context)

def trip_detail(request, slug):
    trip = get_object_or_404(Trip, slug = slug)
    context = {
        'trip': trip,
    }
    return render(request, 'trip_detail.html', context)

def get_drivers(request):
    drivers = list(Driver.objects.values('id','name','surname','date_of_birth', 'slug'))
    return JsonResponse(drivers, safe=False)
def get_cars(request):
    cars = list(Car.objects.values('id', 'make', 'model_name', 'year', 'mileage', 'slug'))
    return JsonResponse(cars, safe=False)
def get_trips(request):
    trips = list(Trip.objects.values('id','start_point', 'end_point','driver_id__name','driver_id__surname', 'car_id__make', 'car_id__model_name', 'start_time', 'end_time','slug'))
    return JsonResponse(trips, safe=False)
