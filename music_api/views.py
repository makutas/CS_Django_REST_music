from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Band
from .serializers import BandSerializer


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
