from django.urls import path
from . import views

urlpatterns = [
    path(
        "accounts/",
        views.ListCreateAccountView.as_view(),
    ),
    path(
        "login/",
        views.FirstLoginView.as_view(),
    )
]