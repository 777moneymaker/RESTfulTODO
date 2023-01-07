from django.db import models

# Create your models here.

class TodoItem(models.Model):
    todo = models.TextField(help_text="Todo name", max_length=80, blank=False, editable=True, unique=True)
    completed = models.BooleanField(default=False, blank=True, editable=True, help_text="Is completed?")

    def __str__(self):
        return f"'{self.todo}', completed?: {self.completed}"