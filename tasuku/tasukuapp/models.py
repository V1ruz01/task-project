from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#someone ate my models :SAJ:
class TaskStatus(models.Model):
    #dumaitesami
    class Status(models.TextChoices):
        TODO = 'To Do'
        DONE = 'Done'
        CANCELLED =  'Cancelled'

    title = models.TextField(max_length=50, default='Tasks')
    desc = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.TODO,)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)


    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title
    

class CommentModel(models.Model):
    task = models.ForeignKey(TaskStatus, on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    media_content = models.FileField(upload_to='media_content/', blank=True, null=True)

    def get_absolute_url(self):
        return self.task.get_absolute_url()
    
