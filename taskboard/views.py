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
    ProjectBoard, ProjectMembership,
)
from .serializers import (
    ProjectBoardSerializer, ProjectBoardDetailSerializer,
)


#Projecy Board
class ProjectBoardAPIView(APIView):
    """
    API view to retrieve project boards for the authenticated user.
    """
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, *args, **kwargs):
        # Filter projects created by user
        created_project = ProjectBoard.objects.filter(creator=request.user)
        # Filter projects where user is a member
        member_projects = ProjectBoard.objects.filter(members=request.user).exclude(creator=request.user)

        created_serializer = ProjectBoardSerializer(created_project, many=True, context={'request': request})
        member_serializer = ProjectBoardSerializer(member_projects, many=True, context={'request': request})

        # Serializer data
        response_data = {
            'created_project': created_serializer.data,
            'member_projects': member_serializer.data,
        }

        # Add messages if the user has no created project or is not part of the project
        if not created_project.exists():
            response_data['created_project_message'] = 'You do not have any project boards yet.'

        if not member_projects.exists():
            response_data['member_projects_message'] = 'You are not participating in any projects yet.'

        return Response(response_data, status=status.HTTP_200_OK)

class ProjectBoardDetailAPIView(APIView):
    """
    API view to retrieve detailed information about a specific project board, including paginated tasks.
    """
    permission_classes = [permissions.IsAuthenticated, ]
    pagination_class = TaskResultsSetPagination

    def get(self, request, slug, *args, **kwargs):
        try:
            # Retrieve the project board by slug
            project_board = ProjectBoard.objects.get(slug=slug)

            # Added check to see if the user is a member of the project or its creator
            if not project_board.members.filter(id=request.user.id).exists() and project_board.creator != request.user:
                return Response({'error': 'You do not have permission to view this project board.'}, status=status.HTTP_403_FORBIDDEN)

            # Serialize the project board data
            serializer = ProjectBoardDetailSerializer(project_board, context={'request': request})
            project_board_data = serializer.data

            # Add a message if there are no tasks associated with the project board
            if not project_board_data['tasks']['results']:
                project_board_data['message'] = 'There are not tasks associated with this project board.'

            return Response(project_board_data, status=status.HTTP_200_OK)
        
        except ProjectBoard.DoesNotExist:
            # Return an error response if the project board does not exist
            return Response({'error': 'Project board not found'}, status=status.HTTP_404_NOT_FOUND)
