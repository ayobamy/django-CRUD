from rest_framework import serializers
from musicapp.models import Song, Artiste, Lyrics

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = "__all__"

class LyricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyrics
        fields = "__all__"
