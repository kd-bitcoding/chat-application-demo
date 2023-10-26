# imports
from dataclasses import field
from unittest.util import _MAX_LENGTH
from rest_framework import serializers

# import model
from user.models import User

# create serializers
class UserSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'active', 'staff', 'admin']
        extra_kwargs = {
            'password' : {'write_only' : True}
        }
    
    def validate(self, attrs):
        password1 = attrs.get('password')
        password2 = attrs.get('password2')
        if password1 != password2:
            raise serializers.ValidationError("Password and confirm password does not match.")
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


# login serializer
class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']

# login serializer
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'active', 'created_at']