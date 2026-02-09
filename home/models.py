from django.db import models

# Create your models here.

class Students(models.Model):
    #id = models.AutoField() -- ye django mai automatice added hoti h and ye table mai serial number add karti and primary key bhi hoti jo kabhi repeat nhi hoti
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    image = models.ImageField()
    file = models.FileField

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField()
    car_count = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.car_name
