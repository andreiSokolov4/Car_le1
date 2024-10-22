import os
from django.db import models

def car_photo_upload_to(instance, filename):
    """Generate folder path based on car year, mark, and model."""
    folder_name = f"{instance.car.year}_{instance.car.mark}_{instance.car.model}".replace(" ", "_")
    return os.path.join('cars', folder_name, 'car_photos', filename)

class Car(models.Model):
    photo = models.ImageField(upload_to=car_photo_upload_to, blank=True, null=True)
    mark = models.CharField(max_length=100, default='Unknown')
    model = models.CharField(max_length=100, default='Unknown')
    price = models.CharField(max_length=11, default='0.00')
    miles = models.CharField(max_length=11, default='0')
    engine = models.CharField(max_length=100, default='Unknown')
    information = models.TextField(blank=True, null=True)
    body = models.CharField(max_length=50, default='Sedan')
    fuel_type = models.CharField(max_length=50, default='Gasoline')
    year = models.IntegerField(default=2021)
    transmission = models.CharField(max_length=50, default='Automatic')
    drive_type = models.CharField(max_length=50, default='Rear-Wheel Drive')
    condition = models.CharField(max_length=50, default='Used')
    engine_size = models.FloatField(default=2.0)
    doors = models.IntegerField(default=4)
    cylinders = models.IntegerField(default=4)
    color = models.CharField(max_length=50, default='Red')
    vin = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return f"{self.mark} {self.model} {self.miles} {self.body}"

    class Meta:
        verbose_name_plural = "Cars"


class Photo(models.Model):
    """Photos for each car are uploaded to the respective car's directory under `car_photos`."""
    car = models.ForeignKey(Car, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=car_photo_upload_to)

    def __str__(self):
        return f"Photo of {self.car.mark} {self.car.model}"
