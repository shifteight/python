from django.db import models

# Create your models here.

importance_choices = (
    ('A', 'Very Important'),
    ('B', 'Important'),
    ('C', 'Medium'),
    ('D', 'Unimportant'),
)


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    importance = models.CharField(
        max_length=1,
        choices=importance_choices
    )