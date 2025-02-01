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
    # Для Ajax форм
    path('add_car/', views.add_car, name='add_car'),
    path('add_driver/', views.add_driver, name='add_driver'),

    path('get_driver_by_id/<int:driver_id>/', views.get_driver_by_id, name='get_driver_by_id'),
    path('get_car_by_id/<int:car_id>/', views.get_car_by_id, name='get_car_by_id'),

    path('delete/driver/<int:driver_id>/', views.delete_driver, name='delete_driver'),
]
