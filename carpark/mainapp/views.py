from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Driver, Trip
from django.db.models import Avg
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def add_car(request):
    if request.method == 'POST':
        try:
            make = request.POST.get('carMake')
            model_name = request.POST.get('carModelName')
            year = request.POST.get('carYear')
            mileage = request.POST.get('carMileage')

            # Валидация данных
            if not make or not model_name or not year or not mileage:
                raise ValidationError('Все поля обязательны для заполнения.')

            # Создаём и сохраняем новый автомобиль
            Car.objects.create(
                make=make,
                model_name=model_name,
                year=year,
                mileage=mileage
            )

            return JsonResponse({'message': 'Данные успешно сохранены!'})
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Ошибка сервера'}, status=500)
        
@csrf_exempt
def add_driver(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('driverName')
            surname = request.POST.get('driverSurname')
            date_of_birth = request.POST.get('driverDoB')  # Строка в формате 'YYYY-MM-DD'
            experience = request.POST.get('driverExp')

            # Отладка
            print(f"Name: {name}, Surname: {surname}, DoB: {date_of_birth}, Exp: {experience}")

            if not name or not surname or not date_of_birth or not experience:
                raise ValidationError('Все поля обязательны для заполнения.')
        
            Driver.objects.create(
                name=name,
                surname=surname,
                date_of_birth=date_of_birth,  # Передаём строку
                experience=experience,
            )

            return JsonResponse({'message': 'Данные успешно сохранены!'})
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            print(f"Ошибка: {e}")  # Отладка
            return JsonResponse({'error': 'Ошибка сервера: ' + str(e)}, status=500)
        