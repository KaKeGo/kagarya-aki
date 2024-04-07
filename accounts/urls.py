from django.urls import path

from .views import (
    GetCSRFTokenApiView, UserStatusAPIView,
    UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView, 
)



app_name = 'accounts'


urlpatterns = [
    path('getcsrftoken/', GetCSRFTokenApiView.as_view(), name='getcsrftoken'),
    path('userstatus/', UserStatusAPIView.as_view(), name='userstatus'),
    path('create/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
]

