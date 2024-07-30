from django.contrib import admin

from .models import (
    ProjectBoard, Task, Subtask, ProjectMembership
)
from .permissions import TaskPermission

# Register your models here.


admin.site.register([ProjectBoard, Task, Subtask, ProjectMembership])
admin.site.register([TaskPermission])
