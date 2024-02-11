from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.middleware.csrf import get_token

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status



@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetCSRFTokenApiView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, *args, **kwargs):
        csrf_token = get_token(request)

        if not csrf_token:
            return Response({'Error': 'CSRFToken has not been retrieved'})

        return Response({'CSRFToken': csrf_token}, status=status.HTTP_200_OK)
