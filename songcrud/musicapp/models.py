from django.db import models
from django.db.models import Model

# Create your models here.
class Artiste(Model):
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    age = models.IntegerField()

class Song(Model):
    title = models.CharField(max_length = 150)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.IntegerField()
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)

class Lyrics(Model):
    content = models.TextField()
    song_id = models.IntegerField()
    Song = models.ForeignKey(Song, on_delete=models.CASCADE)
