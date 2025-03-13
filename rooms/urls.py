from django.urls import path
from . import views

urlpatterns = [
    path("", views.see_all_rooms),
    path("amenities/", views.Amenities.as_view()),
    path("amenities/<int:pk>/", views.AmenityDetail.as_view()),
]
