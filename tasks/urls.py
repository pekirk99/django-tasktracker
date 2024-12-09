from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Home page
    path('add/', views.add_task, name='add_task'),  # Add task page
]
