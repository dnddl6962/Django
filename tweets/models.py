from django.db import models
from common.models import CommonModel

"""Tweet model definition"""


class Tweet(CommonModel):

    payload = models.TextField(
        max_length=180,
    )
    user = models.ForeignKey(
        "users.User",
        models.CASCADE,
        related_name="tweets",
    )

    def __str__(self):
        return f"{self.user.username}'s Tweet"


"""Like model definition"""


class Like(CommonModel):
    user = models.ForeignKey(
        "users.User",
        models.CASCADE,
        related_name="likes",
    )
    tweet = models.ForeignKey(
        "tweets.Tweet",
        models.CASCADE,
        related_name="likes",
    )

    def __str__(self):
        return f"{self.user.username} liked {self.tweet.payload}"
