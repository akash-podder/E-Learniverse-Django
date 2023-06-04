from django.db import models

# Create your models here.
class UserPushedTaskResult(models.Model):
    task_name = models.CharField(max_length=255)
    result = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)