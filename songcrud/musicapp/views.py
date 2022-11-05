from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from musicapp.serializers import SongSerializer, ArtistSerializer
from musicapp.models import Song, Artiste, Lyrics

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('title')
    serializer_class = SongSerializer

class ArtisteViewSet(viewsets.ModelViewSet):
    queryset = Artiste.objects.all().order_by('first_name')
    serializer_class = ArtistSerializer
