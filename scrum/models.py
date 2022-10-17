from django.db import models
from django.conf import settings

# Create your models here.


class Priority(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    description = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        null=True,
    )
