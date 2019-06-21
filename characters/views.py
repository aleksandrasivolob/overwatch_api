from rest_framework import viewsets

from .models import Character
from .serializers import CharacterSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows Overwatch characters to be viewed or edited.
    '''
    queryset = Character.objects.all().order_by('name')
    serializer_class = CharacterSerializer
