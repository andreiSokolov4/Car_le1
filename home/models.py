from django.db import models

class Car(models.Model):
    # your fields
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
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
    car = models.ForeignKey(Car, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_photos/')

    def __str__(self):
        return f"Photo of {self.car.mark} {self.car.model}"
