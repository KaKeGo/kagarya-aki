from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
from .profile_models import UserProfile, Level

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('email', 'is_staff', 'is_active')
    fieldsets = (
        ('Info', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'terms_accepted')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'terms_accepted', 'is_staff', 'is_active', 'is_superuser')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'username', 'get_level')
    search_fields = ('user__email', 'username')
    list_filter = ('level__level',)
    readonly_fields = ('points_needed_for_next_level_display', 'total_experience',)

    fieldsets = (
        ('Info', {'fields': ('user', 'username',)}),
        ('Level', {'fields': ('level', 'experience_points', 'points_needed_for_next_level_display', 'total_experience')}),
        ('Additional info', {'fields': ('avatar', 'bio', 'motto', 'slug',), 'classes': ('collapse',)}),
    )

    def get_level(self, obj):
        return obj.level.level if obj.level else 'No level'
    get_level.admin_order_field = 'level'
    get_level.short_description = 'Level Number'

    def points_needed_for_next_level_display(self, obj):
        return obj.points_needed_for_next_level()
    points_needed_for_next_level_display.short_description = 'Points Needed for Next Level'

    def save_model(self, request, obj, form, change):
        if 'experience_points' in form.changed_data:
            experience_diff = obj.experience_points - (UserProfile.objects.get(id=obj.id).experience_points if obj.id else 0)
            obj.total_experience += experience_diff
        super().save_model(request, obj, form, change)
        obj.check_level_up()



admin.site.register([Level])
admin.site.unregister(Group)
