from django.contrib import admin

from .models import (
    ProjectBoard, Task, Subtask
)
from .permissions import TaskPermission

# Register your models here.


admin.site.register([ProjectBoard, Task, Subtask])
admin.site.register([TaskPermission])
