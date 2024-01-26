from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Celebrity(models.Model):
    name = models.CharField(max_length=150)
    language = models.CharField(max_length=150)
    birthday = models.DateField()
    hobby = models.CharField(max_length=250)
    follow = models.URLField()
    image = models.ImageField(upload_to='celebrity', blank=True)
    

def __str__(self):
        return self.name
