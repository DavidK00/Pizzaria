from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.pizza_name

class Toppings(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping = models.CharField(max_length = 30)

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        return self.topping



