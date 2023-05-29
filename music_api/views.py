from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Band, Album
from .serializers import BandSerializer, AlbumSerializer


# ---------------------------------------------------------BANDS--------------------------------------------------------
@api_view(['GET'])
def get_all_bands(request):
    bands = Band.objects.all()
    serializer = BandSerializer(bands, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_specific_band(request, pk):
    band = Band.objects.get(band_id=pk)
    serializer = BandSerializer(band)
    return Response(serializer.data)


@api_view(['POST'])
def add_band(request):
    serializer = BandSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update_specific_band(request, pk):
    band = Band.objects.get(band_id=pk)
    serializer = BandSerializer(data=request.data, instance=band)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_band(request, pk):
    band = Band.objects.get(band_id=pk)
    name = band.name
    band.delete()
    return Response(f"Band {name} deleted!")


# --------------------------------------------------------ALBUMS--------------------------------------------------------
@api_view(['GET'])
def get_albums(request, band_id):
    albums = Album.objects.filter(band=band_id)
    serializer = AlbumSerializer(albums, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_specific_album(request, album_id):
    album = Album.objects.get(album_id=album_id)
    serializer = AlbumSerializer(album)
    return Response(serializer.data)


@api_view(['POST'])
def create_album(request, band_id):
    serializer = AlbumSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(band_id=band_id)
    return Response(serializer.data)
