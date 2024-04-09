from django.urls import path

from .views import (
    GetCSRFTokenApiView, UserStatusAPIView,
    ActivateAccountAPIVIew,
    UserRegistrationAPIView, UserLoginAPIView, UserLogoutAPIView, 
    ChangePasswordAPIView,
)



app_name = 'accounts'


urlpatterns = [
    path('getcsrftoken/', GetCSRFTokenApiView.as_view(), name='getcsrftoken'),
    path('userstatus/', UserStatusAPIView.as_view(), name='userstatus'),

    path('activate/<str:token>/', ActivateAccountAPIVIew.as_view(), name='activate_account'),

    path('changepassword/', ChangePasswordAPIView.as_view(), name='change_password'),

    path('create/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
]

