from django.db import models


# Create your models here.
class Note(models.Model):
    note = models.CharField(max_length=125)

    def __str__(self):
        return self.note
