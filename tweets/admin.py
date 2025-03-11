from django.contrib import admin
from .models import Tweet, Like


class WordFilter(admin.SimpleListFilter):

    title = "Is the word elon musk included?"

    parameter_name = "Elon_Musk"

    def lookups(self, request, model_admin):
        return [
            ("contains", "Contains"),
            ("not_contains", "Not Contains"),
        ]

    def queryset(self, request, tweet):
        Elon_Musk = self.value()
        if Elon_Musk == "contains":
            return tweet.filter(payload__icontains="elon musk")
        elif Elon_Musk == "not_contains":
            return tweet.exclude(payload__icontains="elon musk")
        return tweet


#


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = (
        "payload",
        "user",
        "total_likes",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "created_at",
        WordFilter,
    )

    search_fields = ("user__username", "payload")

    # def total_likes(self, tweet):
    #     return tweet.likes.count()


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        "tweet",
        "user",
        "created_at",
        "updated_at",
    )

    list_filter = ("created_at",)

    search_fields = ("user__username",)
