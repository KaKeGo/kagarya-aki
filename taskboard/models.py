from django.db import models

# Create your models here.


class ProjectBoard(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    project_board = models.ForeignKey(ProjectBoard, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name
    
class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
