from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

from .models import (
    ProjectBoard,
)
from .serializers import (
    ProjectBoardSerializer,
)


@method_decorator(csrf_protect, name='dispatch')
class ProjectBoardAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        project_board = ProjectBoard.objects.filter(creator=request.user)
        serializer = ProjectBoardSerializer(project_board, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
