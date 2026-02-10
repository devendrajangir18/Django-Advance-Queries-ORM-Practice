from django.db import models
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver

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
    speed = models.IntegerField(default=50)
    car_count = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.car_name


@receiver(post_save , sender= Car)
def call_car_api(sender, instance, **kwargs):
    print("Car Object Created")
    print(sender, instance, kwargs)

    # uncomment car.objects in home.views