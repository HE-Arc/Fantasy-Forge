from django.db import models

# Create your models here.

# for intermediate eval enough:

#User
#Character (for now name enough)
#Class(?)

class Character(models.Model):
    name = models.CharField(max_length=100)
