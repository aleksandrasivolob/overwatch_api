from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100, unique=True)
    character_class = models.CharField(max_length=50)
    ultimate_ability = models.CharField(max_length=100)
    difficulty_of_use = models.IntegerField()
