from rest_framework import serializers

from django.contrib.auth import get_user_model

from accounts.profile_models import UserProfile

from .models import (
    ProjectBoard,
)

User = get_user_model()

class ProjectBoardSerializer(serializers.ModelSerializer):
    creator = serializers.SerializerMethodField()

    class Meta:
        model = ProjectBoard
        fields = ['id', 'name', 'description', 'creator', 'total_tasks', 'completed_tasks', 'slug']

    def get_creator(self, obj):
        user_profile = UserProfile.objects.get(user=obj.creator)
        return user_profile.username if user_profile.username else obj.creator.email
