## --------- [Example 1: Create App Models]-------------------

from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Course(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True) # Ensure that the title field is unique for each Department.
    def __str__(self):
        return self.title