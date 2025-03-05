from django.db import models

from django.contrib.auth.models import User

# for intermediate eval enough:

#User
#Character (for now name enough)
#Class(?)

class Character(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
