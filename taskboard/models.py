import random, string

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from accounts.profile_models import UserProfile
from .permissions import TaskPermission
from .choices import (
    PRIORITY_CHOICES,
    STATUS_CHOICES,
)


User = get_user_model()

# Create your models here.


def generate_random_string(N=10):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))


class ProjectBoard(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            random_string = generate_random_string()
            final_slug = f'{base_slug}-{random_string}'
            while ProjectBoard.objects.filter(slug=final_slug).exists():
                random_string = generate_random_string(len(random_string) + 1)
                final_slug = f'{base_slug}-{random_string}'
            self.slug = final_slug

        super().save(*args, **kwargs)
        is_new = self._state.adding
        if is_new:
            TaskPermission.objects.create(
                user=self.creator,
                project_board=self,
                can_add_task=True,
                can_add_subtask=True,
            )
    
class Task(models.Model):
    project_board = models.ForeignKey(ProjectBoard, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    completed = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            random_string = generate_random_string()
            final_slug = f'{base_slug}-{random_string}'
            while Task.objects.filter(slug=final_slug).exists():
                random_string = generate_random_string(len(random_string) + 1)
                final_slug = f'{base_slug}-{random_string}'
            self.slug = final_slug

        super(Task, self).save(*args, **kwargs)

    def check_completion(self):
        if not self.subtask_set.filter(completed=False).exists():
            self.completed = True
            self.completed_at = timezone.now()
            self.save()
        else:
            if self.completed:
                self.completed = False
                self.completed_at = None
                self.save()
    
class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)

    completed = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    completed_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='completed_subtasks')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='created_subtasks')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.completed and self.completed_at is None:
            self.completed_at = timezone.now()
            self.status = 4

            if not self.completed_by and self.assigned_to:
                self.completed_by = self.assigned_to

            if self.creator:
                try:
                    user_profile = UserProfile.objects.get(user=self.creator)
                    user_profile.add_experience(1)
                except UserProfile.DoesNotExist:
                    pass
            
            if self.completed_by:
                try:
                    completer_profile = UserProfile.objects.get(user=self.completed_by)
                    completer_profile.add_experience(2)
                    completer_profile.save()
                except UserProfile.DoesNotExist:
                    pass

        super(Subtask, self).save(*args, **kwargs)

        all_completed = not self.task.subtask_set.filter(completed=False).exists()

        if all_completed:
            self.task.completed = True
            self.task.completed_at = timezone.now()
            self.task.save(update_fields=['completed', 'completed_at'])

            if self.task.creator:
                try:
                    user_profile = UserProfile.objects.get(user=self.task.creator)
                    user_profile.add_experience(3)
                    user_profile.save()
                except UserProfile.DoesNotExist:
                    pass
    
    def start_working(self, user):
        self.assigned_to = user
        self.status = 3
        self.save()
