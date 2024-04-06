from django.urls import path

from .views import (
    GetCSRFTokenApiView,
    UserRegistrationAPIView,
)



app_name = 'accounts'


urlpatterns = [
    path('getcsrftoken/', GetCSRFTokenApiView.as_view(), name='getcsrftoken'),
    path('create/', UserRegistrationAPIView.as_view(), name='register'),
]

