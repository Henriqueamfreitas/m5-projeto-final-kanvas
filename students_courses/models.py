from django.db import models

# Create your models here.
class StudentCourseStatus(models.TextChoices):
    ACCEPTED = 'accepted'
    DEFAULT = 'pending'

class StudentCourse(models.Model):
    status = models.CharField(
        max_length=11, 
        choices=StudentCourseStatus.choices, 
        default=StudentCourseStatus.DEFAULT
    )
    student = models.ForeignKey(
        "accounts.Account", 
        on_delete=models.CASCADE, 
        related_name="students_courses",
        # db_column="student_id"  
    )
    course = models.ForeignKey(
        "courses.Course", 
        on_delete=models.CASCADE, 
        related_name="students_courses",
        # db_column="course_id"  
    )

    def __str__(self):
        return f"{self.student.username} - {self.course.name}"
