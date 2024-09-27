from django.db import models
from performer.models import Band, Artist

class Album(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()

class Music(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    genre = models.CharField(max_length=255)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    artists = models.ManyToManyField(Artist, through='MusicArtist', related_name='tracks')

class MusicArtist(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, null=True, blank=True)  # Ex: singer, guitarist, etc.
