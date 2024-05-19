from django.db import models
from django.contrib.auth import get_user_model


class TodoModel(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
