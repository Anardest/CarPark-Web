from django.db import models
from slugify import slugify

#TODO: car, driver, trip
class Car(models.Model):
    make = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    year = models.IntegerField()
    mileage = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True)  # Поле для slug

    def save(self, *args, **kwargs): #Автогенерация slug
        if not self.slug:
            self.slug = slugify(f"{self.make}-{self.model_name}-{self.year}")
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.year} {self.make} {self.model_name}"

class Driver(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    experience = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            date_str = self.date_of_birth.strftime('%Y-%m-%d')
            self.slug = slugify(f"{self.name}-{self.surname}-{date_str}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.surname} {self.name} {self.date_of_birth}"

class Trip(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, blank=True, related_name='trip_as_car')
    driver_id = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name='trip_as_driver')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    distance = models.FloatField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            datetime_str = self.start_time.strftime('%Y-%m-%d %H:%M:%S') #Datetime в строку
            self.slug = slugify(f"{self.car_id}-{self.driver_id}-{datetime_str}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Поездка с {self.driver_id} в {self.car_id} с {self.start_time} по {self.end_time}"
