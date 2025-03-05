from rest_framework import serializers
from .models import Character
from django.contrib.auth.models import User

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = [
            "id",
            "name",
        ]
    
    def create(self, validated_data):
        return Character.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
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

    def create(self, validated_data):
        password = validated_data.pop('password') 
        user = User(**validated_data) 
        user.set_password(password)
        user.save()
        return user