from django.urls import path
from . import views

urlpatterns = [
    path("photos/<int:pk>", views.PhotoDetails.as_view()),
]
