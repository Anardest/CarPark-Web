from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Trip

@receiver(post_save, sender = Trip)
def update_car_mileage(sender, instance, **kwargs):
    """
    Обновляет пробег автомобиля при сохранении поездки.
    """
    car = instance.car_id
    car.mileage += abs(instance.distance)
    car.save()