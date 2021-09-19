from django.db import models

# Create your models here.

class EmployeeName(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Paid(models.Model):
    label = models.CharField(max_length=50)
    def __str__(self):
        return self.label

class TADA(models.Model):
    date = models.DateField()
    employee_name = models.ForeignKey(EmployeeName,on_delete=models.CASCADE)
    travel_cost = models.DecimalField(max_digits=6, decimal_places=2)
    lunch_cost = models.DecimalField(max_digits=6, decimal_places=2)
    instruments_cost = models.DecimalField(max_digits=6, decimal_places=2)
    paid = models.ForeignKey(Paid,on_delete=models.CASCADE)









