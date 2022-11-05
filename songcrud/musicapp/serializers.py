from rest_framework import serializers
from musicapp.models import Song, Artiste, Lyrics

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('title')

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ('first_name', 'last_name')

class LyricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyrics
        fields = ('lyrics',)