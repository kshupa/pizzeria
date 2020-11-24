from django.db import models

class Pizza(models.Model):
    """Pizza name."""
    name = models.CharField(max_length=100)

    def __str__(self):
        """Returns pizza name."""
        return self.name


class Topping(models.Model):
    """Pizza toppings."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


    def __str__(self):
        """Returns pizza toppings."""
        return self.name