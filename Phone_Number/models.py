from django.db import models

# Create your models here.


class Phone(models.Model):
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    img = models.IntegerField(default=0)

    def __str__(self):
         return  self.name;
