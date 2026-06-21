from django.db import models
from apps.common.models import BaseModel
from django.utils.safestring import mark_safe

class Todo(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='todos')

    def __str__(self):
        return self.title

    def completed_status(self):
        if self.completed:
            return mark_safe('<span style="color: green;">Completed</span>')
        else:
            return mark_safe('<span style="color: red;">Not Completed</span>')