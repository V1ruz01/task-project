from django import forms
from .models import TaskStatus

class TaskForm(TaskStatus):
    class Meta:
        model = TaskStatus
        fields = ('title', 'desc', 'status')


# add an ability to add images to the tasks

