from django.db import models
import uuid

# Create your models here.
class CourseStatusChoices(models.TextChoices):
    IN_PROGRESS = 'in progress'
    FINISHED = 'finished'
    DEFAULT = 'not started'

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=11, 
        choices=CourseStatusChoices.choices, 
        default=CourseStatusChoices.DEFAULT
    )
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name="courses")
    students = models.ManyToManyField(
        "accounts.Account", 
        through="students_courses.StudentCourse", 
        related_name="enrolled_courses"
    )

    def __str__(self):
        return self.name
