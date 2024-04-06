from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.middleware.csrf import get_token, rotate_token
from django.contrib.auth import logout

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from .serializers import (
    UserRegistrationSerializer, UserLoginSerializer,
)



@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFTokenApiView(APIView):
    '''..CSRF token'''
    permission_classes = (permissions.AllowAny, )

    def get(self, request, *args, **kwargs):
        rotate_token(request)
        csrf_token = get_token(request)

        if not csrf_token:
            return Response({'Error': 'CSRFToken has not been retrieved'})

        return Response({'CSRFToken': csrf_token}, status=status.HTTP_200_OK)

@method_decorator(csrf_protect, name='dispatch')
class UserRegistrationAPIView(APIView):
    '''..Create user account'''
    permission_classes = (permissions.AllowAny, )

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'success': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_protect, name='dispatch')
class UserLoginAPIView(APIView):
    '''..Login user'''
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({'message': 'User logged in successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@method_decorator(csrf_protect, name='dispatch')
class UserLogoutAPIView(APIView):
    '''..Logout user'''
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'User logged out successfully'}, status=status.HTTP_200_OK)
