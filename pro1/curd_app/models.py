from django.db import models


class Employee(models.Model):
    gen = [("MEN", "men"), ("WOMEN", "women"), ("OTHER", "other")]
    employee_id = models.IntegerField()
    name = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=gen, default=True)
    salary = models.FloatField()
    join_date = models.DateField()
    address = models.CharField(max_length=20)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
