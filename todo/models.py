from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title