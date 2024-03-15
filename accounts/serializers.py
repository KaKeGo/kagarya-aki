from rest_framework import serializers

from django.contrib.auth import get_user_model
from .utils import (
    validate_password_length,
)


User = get_user_model()



class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password_confirm', 'terms_accepted']

    def validate_password(self, value):
        password_error = validate_password_length(value)
        if password_error:
            raise serializers.ValidationError(password_error)
        return value

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({'password': 'Passwords are not the same'})
        return data
    
    def create(self, validate_data):
        validate_data.pop('password_confirm', None)
        user = User.objects.create_user(**validate_data)
        return user
