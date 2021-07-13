from django.db import models
import datetime

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField(default=datetime.date.today)
    gender = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()

    def __str__(self):
        return self.name
