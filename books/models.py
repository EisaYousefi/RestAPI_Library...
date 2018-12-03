from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)


    def __str__(self):
        return  self.book_name

