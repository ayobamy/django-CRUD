from django.db import models
from django.db.models import Model

# Create your models here.
class Song(Model):
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    age = models.IntegerField()

class Artiste(Model):
    title = models.CharField(max_length = 150)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Song, on_delete = models.CASCADE)

class Lyrics(Model):
    pass

