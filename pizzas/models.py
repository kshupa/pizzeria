from django.db import models

class Pizza(models.Model):
    """Pizza name."""
    name = models.CharField(max_length=100)


class Topping(models.Model):
    """Pizza toppings."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
