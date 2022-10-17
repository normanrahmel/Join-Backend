from django.contrib import admin
from . import models


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "category", "priority", "description", "user")


# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Priority)
admin.site.register(models.Task, TaskAdmin)
