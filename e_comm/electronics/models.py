from django.db import models

# Create your models here.

class laptops(models.Model):
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    prize = models.IntegerField()

    def __str__(self):
        return self.model
