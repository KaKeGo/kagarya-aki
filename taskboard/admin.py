from django.contrib import admin

from .models import (
    ProjectBoard, Task, Subtask
)

# Register your models here.


admin.site.register([ProjectBoard, Task, Subtask])
