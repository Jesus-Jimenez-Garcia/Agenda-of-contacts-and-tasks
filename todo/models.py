from django.db import models
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator

class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(default=date.today)
    estimated_end = models.DateField(blank=True, null=True)
    priority = models.IntegerField(default=3, validators=[
        MaxValueValidator(5),
        MinValueValidator(1),
    ])

    def __str__(self):
        return self.title