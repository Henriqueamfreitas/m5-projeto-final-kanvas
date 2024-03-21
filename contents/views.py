from courses.models import Course
from .models import Content
from .serializers import ContentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class ListCreateContentView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        course_id = self.kwargs.get('course_id') 
        course = Course.objects.get(id=course_id)
        serializer.save(course=course)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Content.objects.all()
        return Content.objects.filter(course=self.request.user)


class RetrieveUpdateDeleteContentView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

