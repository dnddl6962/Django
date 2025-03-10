from django.contrib import admin
from .models import Tweet, Like


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = (
        "payload",
        "user",
        "total_likes",
        "created_at",
        "updated_at",
    )

    def total_likes(self, tweet):
        return tweet.likes.count()


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        "tweet",
        "user",
        "created_at",
        "updated_at",
    )
