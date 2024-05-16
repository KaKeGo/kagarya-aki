import jwt

from django.conf import settings
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.middleware.csrf import get_token, rotate_token
from django.contrib.auth import logout, login, get_user_model
from django.shortcuts import redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from .utils import (
    send_activation_email, send_reset_password_email,
)
from .profile_models import UserProfile
from .serializers import (
    UserRegistrationSerializer, UserLoginSerializer,
    ChangePasswordSerializer, PasswordResetSerializer, SetNewPasswordSerializer,
)

User = get_user_model()


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFTokenApiView(APIView):
    # ..CSRF token
    permission_classes = (permissions.AllowAny, )

    def get(self, request, *args, **kwargs):
        rotate_token(request)
        csrf_token = get_token(request)

        if not csrf_token:
            return Response({'Error': 'CSRFToken has not been retrieved'})

        return Response({'CSRFToken': csrf_token}, status=status.HTTP_200_OK)

class UserStatusAPIView(APIView):
    # ..User status check if user is logged in or anonymous
    permission_classes = [permissions.AllowAny, ]

    def get(self, request, *args, **kwargs):
        is_authenticated = request.user.is_authenticated
        if is_authenticated:
            user_profile = UserProfile.objects.get(user=request.user)
            username_or_email = user_profile.username if user_profile.username else request.user.email
            
            return Response({
                    'is_authenticated': is_authenticated,
                    'status': 'User is logged in',
                    'email': request.user.email,
                    'username_or_email': username_or_email,
                 }, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'User is anonymous'}, status=status.HTTP_200_OK)

class ActivateAccountAPIVIew(APIView):
    # ..Activate account for user registration
    permission_classes = (permissions.AllowAny, )

    def get(self, request, *args, **kwargs):
        token = kwargs.get('token', '')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_active:
                user.is_active = True
                user.save()
                return redirect(f"{settings.FRONTEND_DEV_URL}")
            else:
                return redirect(f"{settings.FRONTEND_DEV_URL}")
        except jwt.ExpiredSignatureError:
            return redirect(f"{settings.FRONTEND_DEV_URL}")
        except (jwt.DecodeError, User.DoesNotExist):
            return redirect(f"{settings.FRONTEND_DEV_URL}")

@method_decorator(csrf_protect, name='dispatch')
class UserRegistrationAPIView(APIView):
    # ..Create user account
    permission_classes = (permissions.AllowAny, )

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_activation_email(user)
            return Response({'success': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_protect, name='dispatch')
class UserLoginAPIView(APIView):
    # ..Login user
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response({'message': 'User logged in successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@method_decorator(csrf_protect, name='dispatch')
class UserLogoutAPIView(APIView):
    # ..Logout user
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'User logged out successfully'}, status=status.HTTP_200_OK)

@method_decorator(csrf_protect, name='dispatch')
class ChangePasswordAPIView(APIView):
    # ..User change password
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_protect, name='dispatch')
class PasswordResetAPIView(APIView):
    # ..User password reset
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = User.objects.filter(email=email).first()
            if user:
                send_reset_password_email(user)
                return Response({'message': 'If an account with that email exists, we have sent an email to reset your password'}, status=status.HTTP_200_OK)
            return Response({'error': 'User with this email does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_protect, name='dispatch')
class PasswordResetConfirmAPIView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        token = request.data.get('token')
        serializer = SetNewPasswordSerializer(data=request.data)
        if serializer.is_valid():
            new_password = serializer.validated_data['new_password']
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                user = User.objects.get(id=payload['user_id'])
                user.set_password(new_password)
                user.save()
                return Response({'message': 'Passsword has been reset successfully'}, status=status.HTTP_200_OK)
            except jwt.ExpiredSignatureError:
                return Response({'error': 'Token expired'}, status=status.HTTP_400_BAD_REQUEST)
            except jwt.DecodeError:
                return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
