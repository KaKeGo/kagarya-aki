from django.db import models
from django.contrib.auth import get_user_model

from .models import ProjectBoard
from accounts.profile_models import UserProfile

User = get_user_model()


class TaskPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_board = models.ForeignKey('ProjectBoard', on_delete=models.CASCADE)
    can_add_task = models.BooleanField(default=False)
    can_add_subtask = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'project_board')

    def __str__(self):
        permissions = []
        if self.can_add_task:
            permissions.append('add tasks')
        if self.can_add_subtask:
            permissions.append('add subtasks')
        user_profile = UserProfile.objects.get(user=self.user)
        return f'{user_profile.username} can {", ".join(permissions)} for {self.project_board.name}'
