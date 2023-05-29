from rest_framework import serializers
from .models import Band, Album


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    band_id = serializers.ReadOnlyField(source='band_id.id')

    class Meta:
        model = Album
        fields = ['album_id', 'band_id', 'name', 'year']
