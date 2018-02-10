from django.db import models
from django.db.models import SET_NULL


class Artist(models.Model):
    name = models.CharField(max_length=127)
    year = models.IntegerField()


class Song(models.Model):
    artist = models.ForeignKey(Artist, null=True, on_delete=SET_NULL)
    name = models.CharField(max_length=127)
    genre = models.CharField(max_length=64, blank=True, null=True)
