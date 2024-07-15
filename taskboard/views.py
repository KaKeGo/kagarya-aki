from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

from .models import (
    ProjectBoard,
)
from .serializers import (
    ProjectBoardSerializer, ProjectBoardDetailSerializer,
)


class ProjectBoardAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        project_board = ProjectBoard.objects.filter(creator=request.user)
        if not project_board.exists():
            return Response({'message': 'You do not have any project boards yet.'}, status=status.HTTP_200_OK)

        serializer = ProjectBoardSerializer(project_board, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProjectBoardDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, slug, *args, **kwargs):
        try:
            project_board = ProjectBoard.objects.get(slug=slug)
            serializer = ProjectBoardDetailSerializer(project_board)
            response_data = serializer.data

            if not response_data['task']:
                response_data['message'] = 'There are not tasks associated with this project board.'

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except ProjectBoard.DoesNotExist:
            return Response({'error': 'Project board not found'}, status=status.HTTP_404_NOT_FOUND)
