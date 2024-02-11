from django.urls import path

from .views import (
    GetCSRFTokenApiView,
)



app_name = 'accounts'


urlpatterns = [
    path('getcsrftoken/', GetCSRFTokenApiView.as_view(), name='getcsrftoken'),
]

