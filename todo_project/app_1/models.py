from django.db import models


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    def complete_task(self):
        CompletedTask.objects.create(
            task_id=self.id,
            title=self.title,
            description=self.description,
            completed_at=self.due_date,
        )
        self.delete()

    def __str__(self):
        return self.title


class CompletedTask(models.Model):
    task_id = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task_id} - {self.completed_at} - {self.title}"
