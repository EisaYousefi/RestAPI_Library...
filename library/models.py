from django.db import models

# Create your models here.

class Books(models.Model):
    id         = models.CharField(primary_key=True,max_length=50)
    bookName   = models.CharField(max_length=300)
    authorName = models.CharField(max_length=300)
    publishers = models.CharField(max_length=300)
    price      = models.IntegerField(default=0)


    def __str__(self):
        return  self.bookName



class Azo(models.Model):

    id_azo    = models.CharField(primary_key=True,max_length=50)
    nameFamil = models.CharField(max_length=300)
    tel       = models.CharField(max_length=20)

    def __str__(self):
        return self.nameFamil


class Amanat(models.Model):
    name_book_amanat       = models.CharField(max_length=300)
    id_book_amanat         = models.CharField(primary_key=True,max_length=50)
    writername_book_amanat = models.CharField(max_length=300)
    tel_amanat             = models.CharField(max_length=25)
    name_amanat            = models.CharField(max_length=300)
    id_name_amanat         = models.CharField(max_length=30)

    def __str__(self):
        return self.name_book_amanat






