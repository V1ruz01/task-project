from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


#someone ate my models :SAJ:
class TaskStatus(models.Model):
    #dumaitesami
    class Status(models.TextChoices):
        TODO = 'To Do'
        DONE = 'Done'
        CANCELLED =  'Cancelled'

    class Priority(models.TextChoices):
        LOW = 'low', 'Low'
        MEDIUM = 'medium', 'Medium'
        HIGH = 'high', 'High'

    title = models.TextField(max_length=50, default='Tasks')
    desc = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.TODO,)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.MEDIUM)
    due_date = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title

    @property
    def completed(self):
        return self.status == self.Status.DONE
    

class CommentModel(models.Model):
    task = models.ForeignKey(TaskStatus, on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    media_content = models.FileField(upload_to='media_content/', blank=True, null=True)

    def get_absolute_url(self):
        return self.task.get_absolute_url()
    
