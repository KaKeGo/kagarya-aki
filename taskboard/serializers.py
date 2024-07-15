from rest_framework import serializers

from django.contrib.auth import get_user_model

from accounts.profile_models import UserProfile

from .models import (
    ProjectBoard, Task,
)

User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'created_at', 'completed_at', 'status', 'priority', 'completed', 'creator', 'slug']

class ProjectBoardSerializer(serializers.ModelSerializer):
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
    task = TaskSerializer(many=True, read_only=True, source='task_set')
    
    class Meta:
        model = ProjectBoard
        fields = ['id', 'name', 'description', 'task', 'creator', 'total_tasks', 'completed_tasks', 'slug']
