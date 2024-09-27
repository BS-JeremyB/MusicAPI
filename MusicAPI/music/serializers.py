from rest_framework import serializers
from .models import Music, Album, MusicArtist
from performer.models import Artist, Band

class MusicArtistSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(view_name='artist-detail', queryset=Artist.objects.all())

    class Meta:
        model = MusicArtist
        fields = ['url', 'artist', 'role']

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    tracks = serializers.HyperlinkedRelatedField(view_name='music-detail', many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['url', 'name', 'year', 'tracks']

class MusicSerializer(serializers.HyperlinkedModelSerializer):
    album = serializers.HyperlinkedRelatedField(view_name='album-detail', queryset=Album.objects.all())
    band = serializers.HyperlinkedRelatedField(view_name='band-detail', queryset=Band.objects.all())
    artists = MusicArtistSerializer(source='musicartist_set', many=True)

    class Meta:
        model = Music
        fields = ['url', 'name', 'year', 'genre', 'band', 'album', 'artists']


    def create(self, validated_data):
        artists_data = validated_data.pop('musicartist_set')
        music = Music.objects.create(**validated_data)
        for artist_data in artists_data:
            MusicArtist.objects.create(music=music, **artist_data)
        return music
    
    def update(self, instance, validated_data):
        artists_data = validated_data.pop('musicartist_set')
        instance = super().update(instance, validated_data)
        for artist_data in artists_data:
            MusicArtist.objects.create(music=instance, **artist_data)
        return instance