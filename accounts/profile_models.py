from django.db import models
from django.contrib.auth import get_user_model

from .lvl_info import LevelInfo


User = get_user_model()


def get_default_avatar():
    '''Default avatar for users'''
    return 'default/avatar/avatar.jpg'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=45, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', default=get_default_avatar,blank=True, null=True)
    motto = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(max_length=5000, blank=True, null=True)

    level = models.ForeignKey('Level', on_delete=models.SET_NULL, null=True, blank=True)
    experience_points = models.IntegerField(default=0)
    total_experience = models.IntegerField(default=0)

    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.user.email
    
    def add_experience(self, points):
        self.experience_points += points
        self.total_experience += points
        self.save()
        self.check_level_up()

    def check_level_up(self):
        while self.level and self.experience_points >= self.level.experience_required:
            excess_experience = self.experience_points - self.level.experience_required
            
            next_level, created = Level.objects.get_or_create(
                level=self.level.level + 1,
                defaults={'experience_required': self.level.experience_required + 5}
            )
            
            self.level = next_level

            self.experience_points = excess_experience
            self.save()

    def points_needed_for_next_level(self):
        if not self.level:
            return None
        points_for_next_level = 10
        points_increase_per_level = 5
        required_points_for_next_level = points_for_next_level + (self.level.level - 1) * points_increase_per_level
      
        return required_points_for_next_level - self.experience_points
    
    def get_level_info(self):
        if self.level:
            color, title = LevelInfo.get_info_for_level(self.level.level)
            return color, title
        return 'No title', 'No Color'

class Level(models.Model):
    level = models.IntegerField(default=1)
    experience_required = models.IntegerField(default=10)

    def __str__(self):
        return f'Level {self.level}'
