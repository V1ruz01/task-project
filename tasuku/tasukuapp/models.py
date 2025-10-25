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


    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title