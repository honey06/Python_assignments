# myapp/models.py
from django.db import models


class Department(models.Model):
    department_id = models.CharField(max_length=100, unique=True)
    department_name = models.CharField(max_length=200)
    manager = models.ForeignKey(
        'Employee',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='departments'
    )

    def __str__(self):
        return self.department_name


class Employee(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

    def __str__(self):
        return self.name
