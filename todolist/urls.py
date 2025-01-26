from django.urls import path
from .views import task, form, update, edit, delete_task  # Ensure delete_task is imported

urlpatterns = [
    path('task/', task, name='task'),  # List all tasks
    path('form/', form, name='form'),  # Add a new task
    path('task/complete/<int:pk>/', update, name='update_task'),  # Mark task as completed
    path('task/edit/<int:pk>/', edit, name='edit_task'),  # Edit task
    path('task/delete/<int:pk>/', delete_task, name='delete_task'),  # Delete task
]
