from django.urls import path

from .views import (
    GetCSRFTokenApiView, UserStatusAPIView,
    ActivateAccountAPIVIew,
    UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView, 
)



app_name = 'accounts'


urlpatterns = [
    path('getcsrftoken/', GetCSRFTokenApiView.as_view(), name='getcsrftoken'),
    path('userstatus/', UserStatusAPIView.as_view(), name='userstatus'),

    path('activate/<str:token>/', ActivateAccountAPIVIew.as_view(), name='activate_account'),

    path('create/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
]

