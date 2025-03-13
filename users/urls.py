from django.urls import path
from tweets import views

urlpatterns = [
    path("<int:user_id>/tweets/", views.user_tweets),
]
