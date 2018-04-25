from django.shortcuts import render, render_to_response

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from audiolibary.models import Song
from audiolibary.serializers import SongSerializer


def get_songs(request):
    songs = Song.objects.all()
    return render_to_response('index.html', context={'songs': songs})


class SongViewSet(ModelViewSet):
    """
    very good view set
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
