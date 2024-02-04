from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .profile_models import UserProfile, Level


User = get_user_model()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        default_level, created = Level.objects.get_or_create(level=1)
        UserProfile.objects.create(user=instance, level=default_level)
    else:
        instance.userprofile.save()
