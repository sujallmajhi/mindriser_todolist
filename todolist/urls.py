from django.urls import path
from .views import task, form, update

urlpatterns = [
    path('task/', task, name='task'),  # This will show the tasks list
    path('form/', form, name='form'),  # Form for adding new tasks
    path('task/<int:pk>/', update, name="task"),  # Update task status (use <int:pk> to capture the task ID)
]
