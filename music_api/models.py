from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Band(models.Model):
    band_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='albums')
    name = models.CharField(max_length=100)
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(9999)])

    def __str__(self):
        return self.name


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    name = models.CharField(max_length=100)
    duration = models.FloatField()

    def __str__(self):
        return f'{self.name} - {self.duration}'
