from django.urls import path
from . import views

urlpatterns = [
    path(
        "perks/", views.Perks.as_view()
    ),  # class를 가져오려면 as_view()를 호출해야함 -> Just Rule!
    path(
        "perks/<int:pk>/",
        views.PerkDetail.as_view(),
    ),
]
