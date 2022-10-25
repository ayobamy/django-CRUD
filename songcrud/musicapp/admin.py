from django.contrib import admin

# Register your models here.
from musicapp.models import Song, Artiste, Lyrics

admin.site.register(Song)
admin.site.register(Artiste)
admin.site.register(Lyrics)
