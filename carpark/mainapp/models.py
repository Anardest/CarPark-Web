from django.db import models

#TODO: car, driver, trip
class Car(models.Model):
    make = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    year = models.IntegerField()
    mileage = models.IntegerField()

    def __str__(self):
        return f"{self.year} {self.make} {self.model_name}"

class Driver(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    experience = models.IntegerField()

    def __str__(self):
        return f"{self.surname} {self.name} {self.date_of_birth}"

class Trip(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, blank=True)
    driver_id = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    distance = models.FloatField()

    def __str__(self):
        return f"Поездка с {self.driver_id} в {self.car_id} с {self.start_time} по {self.end_time}"
