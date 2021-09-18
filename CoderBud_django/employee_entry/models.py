from django.db import models

# Create your models here.

class TADA(models.Model):
    date = models.DateField()
    employee_name = models.CharField(max_length=255)
    travel_cost = models.DecimalField(max_digits=6, decimal_places=2)
    lunch_cost = models.DecimalField(max_digits=6, decimal_places=2)
    instruments_cost = models.DecimalField(max_digits=6, decimal_places=2)
    paid = models.BooleanField()

    







