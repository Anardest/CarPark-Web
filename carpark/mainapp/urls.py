from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cars/<slug:slug>/', views.car_detail, name='car_detail'),
    path('drivers/<slug:slug>/', views.driver_detail, name='driver_detail'),
    path('trips/<slug:slug>/', views.trip_detail, name='trip_detail'),
    # Для Ajax вывода данных на главной странице
    path('get_drivers/', views.get_drivers, name='get_drivers'),
    path('get_cars/', views.get_cars, name='get_cars'),
    path('get_trips/', views.get_trips, name='get_trips'),
]
