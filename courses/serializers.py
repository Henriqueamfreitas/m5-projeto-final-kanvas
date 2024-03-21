from rest_framework import serializers
from accounts.serializers import AccountSerializer
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    instructor = serializers.UUIDField(source='instructor.id', read_only=True, required=False, allow_null=True)
    contents = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    students_courses = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            "id", 
            "instructor", 
            "contents", 
            "students_courses", 
            "name", 
            "status", 
            "start_date", 
            "end_date"
        ]
