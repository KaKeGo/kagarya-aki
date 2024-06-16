from django.urls import path

from .views import (
    ProjectBoardAPIView,
)


app_name = 'task_board'


urlpatterns = [
    path('', ProjectBoardAPIView.as_view(), name='projectboard'),
]
