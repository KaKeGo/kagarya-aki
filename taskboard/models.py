import random, string

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth import get_user_model


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
        super(ProjectBoard, self).save(*args, **kwargs)
    
class Task(models.Model):
    project_board = models.ForeignKey(ProjectBoard, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    completed = models.BooleanField(default=True)
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

        if self.completed and not self.completed_at:
            self.completed_at = timezone.now()
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

    completed = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.completed and not self.completed_at:
            self.completed_at = timezone.now()
        super(Subtask, self).save(*args, **kwargs)
