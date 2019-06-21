from rest_framework import serializers

from .models import Character

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ('name', 'character_class', 'ultimate_ability', 'difficulty_of_use')
