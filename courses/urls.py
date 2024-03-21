from django.urls import path
from . import views

urlpatterns = [
    path(
        "courses/",
        views.ListCreateCourseView.as_view(),
    ),
    path(
        "courses/<int:course_id>/",
        views.RetrieveUpdateDeleteCourseView.as_view(),
    ),
]