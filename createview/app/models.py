from django.db import models
from django.urls import reverse
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reversed("thankyou")
