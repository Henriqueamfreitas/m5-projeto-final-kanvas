from django.db import models
import uuid

# Create your models here.
class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150) 
    content = models.TextField()
    video_url = models.CharField(max_length=200, null=True, blank=True)
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE, related_name="contents")

    def __str__(self):
        return f"Content {self.id} - {self.course.name}"

