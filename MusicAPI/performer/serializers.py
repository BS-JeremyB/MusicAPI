from rest_framework import serializers
from .models import Artist, Band

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ['url', 'first_name', 'name', 'genre', 'origin', 'birth_date']

class BandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Band
        fields = ['url', 'name', 'genre', 'origin', 'formation_year']