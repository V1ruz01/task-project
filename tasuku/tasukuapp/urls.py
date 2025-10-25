#make pathes here
from django.urls import path

from .views import *

app_name = 'tasukuapp'

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('task/create', TaskCreateView.as_view(), name='task_create'),
    path('task/update/<int:pk>', TaskUpdateView.as_view(), name='task_update'),
    path('task/delete/<int:pk>', TaskDeleteView.as_view(), name='task_detele'),
    path('register/', RegisterView.as_view(), name='register'),
]