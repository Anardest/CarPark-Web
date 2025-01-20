from django.shortcuts import render, get_object_or_404
from .models import Car

def index(request): #Главная страница
    cars = Car.objects.all()
    context = {
        # 'context' : 'Имя',
        # 'date': datetime.now(),
        'cars' : cars
    }
    return render(request, "index.html", context)

def car_detail(request, slug):
    car = get_object_or_404(Car, slug = slug)
    context = {
        'car': car,
    }
    return render(request, 'car_detail.html', context)
