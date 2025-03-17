from django.urls import path
from . import views

urlpatterns = [
    path("", views.Tweets.as_view()),
    path("<int:pk>", views.OneTweet.as_view()),
]

# render
# urlpatterns = [
#     path("", views.see_all_tweets),
#     path("<int:tweet_pk>", views.see_one_tweet),
# ]
