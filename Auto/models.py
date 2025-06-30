from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    rate = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(6)])
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name
