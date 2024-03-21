from rest_framework import serializers
from accounts.serializers import AccountSerializer
from .models import Content

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = [
            "id", 
            "name", 
            "content", 
            "video_url"
        ]
