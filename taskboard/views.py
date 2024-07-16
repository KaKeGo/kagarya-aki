from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.pagination import PageNumberPagination

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

from kagarya.pagination import (
    TaskResultsSetPagination,
)
from .models import (
    ProjectBoard, Task
)
from .serializers import (
    ProjectBoardSerializer, ProjectBoardDetailSerializer,
    TaskSerializer,
)


#Projecy Board
class ProjectBoardAPIView(APIView):
    """
    API view to retrieve project boards for the authenticated user.
    """
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        project_board = ProjectBoard.objects.filter(creator=request.user)
        if not project_board.exists():
            return Response({'message': 'You do not have any project boards yet.'}, status=status.HTTP_200_OK)

        serializer = ProjectBoardSerializer(project_board, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProjectBoardDetailAPIView(APIView):
    """
    API view to retrieve detailed information about a specific project board, including paginated tasks.
    """
    permission_classes = [permissions.IsAuthenticated, ]
    pagination_class = TaskResultsSetPagination

    def get(self, request, slug, *args, **kwargs):
        try:
            project_board = ProjectBoard.objects.get(slug=slug)
            serializer = ProjectBoardDetailSerializer(project_board, context={'request': request})
            project_board_data = serializer.data

            if not project_board_data['tasks']['results']:
                project_board_data['message'] = 'There are not tasks associated with this project board.'

            return Response(project_board_data, status=status.HTTP_200_OK)
        
        except ProjectBoard.DoesNotExist:
            return Response({'error': 'Project board not found'}, status=status.HTTP_404_NOT_FOUND)
