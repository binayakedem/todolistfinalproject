from typing import Any
from django.db import models
# Create your models here.


class Task(models.Model):
    name=models.CharField(max_length=20)
    mission=models.TextField()
    startDate=models.DateField()
    duration=models.IntegerField()
    isCompleted=models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.name
        