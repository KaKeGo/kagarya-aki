from django.db import models
from django.contrib.auth import get_user_model

from accounts.profile_models import UserProfile

User = get_user_model()


class TaskPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_board = models.ForeignKey('taskboard.ProjectBoard', on_delete=models.CASCADE)
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

        from .models import ProjectBoard
        project_board = ProjectBoard.objects.get(id=self.project_board_id)

        creator_email = self.project_board.creator.email if self.project_board.creator else 'Unknown User'
    
        project_board_name = self.project_board.name if self.project_board.name else 'Unknown Project'

        return f'{creator_email} can {", ".join(permissions)} for {project_board_name}'
