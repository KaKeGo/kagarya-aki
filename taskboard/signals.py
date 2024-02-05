from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Subtask


@receiver(post_save, sender=Subtask)
def update_task_status(sender, instance, **kwargs):
    instance.task.check_completion()
