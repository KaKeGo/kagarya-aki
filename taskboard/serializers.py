from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import (
    ProjectBoard,
)

User = get_user_model()

class ProjectBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectBoard
        fields = ['id', 'name', 'description', 'creator', 'total_tasks', 'completed_tasks']
