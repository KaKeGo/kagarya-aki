from rest_framework import serializers

from django.contrib.auth import get_user_model

from accounts.profile_models import UserProfile

from kagarya.pagination import (
    TaskResultsSetPagination,
)
from .models import (
    ProjectBoard, Task,
)

User = get_user_model()


#Task
class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model.
    Provides additional fields for status, priority, and creator display.
    """
    status_display = serializers.SerializerMethodField()
    priority_display = serializers.SerializerMethodField()
    creator_display = serializers.SerializerMethodField()
    
    class Meta:
        model = Task
        fields = ['id', 'name', 'created_at', 'completed_at', 'status_display', 'priority_display', 'completed', 'creator_display', 'slug']

    def get_status_display(self, obj):
        return obj.get_status_display()
    
    def get_priority_display(self, obj):
        return obj.get_priority_display()
    
    def get_creator_display(self, obj):
        user_profile = UserProfile.objects.get(user=obj.creator)
        return user_profile.username if user_profile.username else obj.creator.email

#Project Board
class ProjectBoardSerializer(serializers.ModelSerializer):
    """
    Serializer for ProjectBoard model.
    Provides additional fields for creator and short description.
    """
    creator = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name='task_board:projectboard_detail', lookup_field='slug')

    class Meta:
        model = ProjectBoard
        fields = ['id', 'name', 'short_description', 'creator', 'total_tasks', 'completed_tasks', 'slug', 'url']

    def get_creator(self, obj):
        user_profile = UserProfile.objects.get(user=obj.creator)
        return user_profile.username if user_profile.username else obj.creator.email
    
    def get_short_description(self, obj):
        if len(obj.description) > 60:
            return obj.description[:60] + '...'
        return obj.description

class ProjectBoardDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for detailed view of ProjectBoard model.
    Provides additional fields for tasks and creator display.
    """
    tasks = serializers.SerializerMethodField()
    creator_display = serializers.SerializerMethodField()
    
    class Meta:
        model = ProjectBoard
        fields = ['id', 'name', 'description', 'creator_display', 'tasks', 'total_tasks', 'completed_tasks', 'slug']

    def get_tasks(self, obj):
        request = self.context.get('request')
        paginator = TaskResultsSetPagination()
        tasks = Task.objects.filter(project_board=obj)
        paginated_tasks = paginator.paginate_queryset(tasks, request)
        serializer = TaskSerializer(paginated_tasks, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data).data
    
    def get_creator_display(self, obj):
        user_profile = UserProfile.objects.get(user=obj.creator)
        return user_profile.username if user_profile.username else obj.creator.email
