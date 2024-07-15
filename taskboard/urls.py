from django.urls import path

from .views import (
    ProjectBoardAPIView, ProjectBoardDetailAPIView,
)


app_name = 'task_board'


urlpatterns = [
    path('', ProjectBoardAPIView.as_view(), name='projectboard'),
    path('<slug:slug>/', ProjectBoardDetailAPIView.as_view(), name='projectboard_detail'),
]
