from rest_framework import serializers
from .models import Character, Ownership
from django.contrib.auth.models import User

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class CharacterSerializer(serializers.ModelSerializer):

    owners = serializers.SerializerMethodField()

    class Meta:
        model = Character
        fields = [
            "id",
            "name",
            "strength",
            "constitution",
            "dexterity",
            "intelligence",
            "wisdom",
            "charisma",
            "biography",
            "owners"
        ]

    def get_owners(self, obj):
        """Return a list of usernames who own the character"""
        return [ownership.user.username for ownership in obj.ownership_set.all()]
    
    def create(self, validated_data):
        """Ensure the character is created for the logged-in user"""
        user = self.context["request"].user  # Get authenticated user
        character = Character.objects.create(**validated_data)

        # authomatically create ownership object for the creator
        Ownership.objects.create(user=user, character=character)
        return character
    


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        """
        Validate password against Django's password validators.
        """
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def validate_email(self, value):
        """
        Validate email format.
        """
        if not value or "@" not in value:
            raise serializers.ValidationError("Invalid email format.")
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        if len(value) > 254:
            raise serializers.ValidationError("Email address is too long.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    


class OwnershipSerializer(serializers.ModelSerializer):

    character_name = serializers.ReadOnlyField(source="character.name")  

    class Meta:
        model = Ownership
        fields = ["id", "user", "character", "date_added", "character_name"]
        read_only_fields = ["date_added"]