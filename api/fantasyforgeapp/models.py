from django.db import models

from django.contrib.auth.models import User


class Character(models.Model):
    CLASS_CHOICES = [
        ('Barbarian', 'Barbarian'),
        ('Bard', 'Bard'),
        ('Cleric', 'Cleric'),
        ('Druid', 'Druid'),
        ('Fighter', 'Fighter'),
        ('Monk', 'Monk'),
        ('Paladin', 'Paladin'),
        ('Ranger', 'Ranger'),
        ('Rogue', 'Rogue'),
        ('Sorcerer', 'Sorcerer'),
        ('Warlock', 'Warlock'),
        ('Wizard', 'Wizard'),
    ]
    
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=20, choices=CLASS_CHOICES, default='Barbarian')
    strength = models.IntegerField(default=0)
    constitution= models.IntegerField(default=0)
    dexterity= models.IntegerField(default=0)
    intelligence= models.IntegerField(default=0)
    wisdom= models.IntegerField(default=0)
    charisma = models.IntegerField(default=0)
    biography = models.TextField(default="no biography")
    owners = models.ManyToManyField(User, through='Ownership', related_name='characters')


class Ownership(models.Model):
    """Many-to-Many Relationship between Users and Characters"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    character = models.ForeignKey(Character, on_delete=models.CASCADE) 
    date_added = models.DateTimeField(auto_now_add=True) 

    class Meta:
        unique_together = ("user", "character")  # Ensure each user can only own a character once

    def __str__(self):
        return f"{self.user.username} owns {self.character.name}"
