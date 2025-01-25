from django.urls import path
from .views import *

urlpatterns = [
    path('task/',task, name='task'),  # Add the 'name' here
    path('form/',form, name='form'),  # Optionally name the form view too
]
