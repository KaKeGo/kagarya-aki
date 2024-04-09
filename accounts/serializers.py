from django.contrib.auth import authenticate

from rest_framework import serializers

from django.contrib.auth import get_user_model
from .utils import (
    validate_password_length, validate__email,
)


User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):  
    '''..Create user account'''
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    terms_accepted = serializers.BooleanField(required=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password_confirm', 'terms_accepted']

    def validate_email(self, value):
        email_error = validate__email(value)
        if email_error:
            raise serializers.ValidationError(email_error)
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with this email already exists.")
    
        return value

    def validate_password(self, value):
        password_error = validate_password_length(value)
        if password_error:
            raise serializers.ValidationError(password_error)
        return value

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({'password_confirm': ['Passwords are not the same']})
        return data
    
    def create(self, validate_data):
        validate_data.pop('password_confirm', None)
        user = User.objects.create_user(**validate_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    '''..Login user '''
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(request=self.context.get('request'), username=email, password=password)

        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'There is no account with this email'})
           
        if not user:
            raise serializers.ValidationError({'password': 'Wrong password!!'})
        
        data['user'] = user
        return data

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError('Old password is incorrect')
        return value

    def validate(self, data):
        if data['new_password'] != data['confirm_new_password']:
            raise serializers.ValidationError({'confirm_new_password': 'New password must match'})
        validate_password_length(data['new_password'])
        return data
