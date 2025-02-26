from django.db import models
from common.models import CommonModel


class ChattingRoom(CommonModel):
    """Room Model Definition"""

    users = models.ManyToManyField(
        "users.User",
        related_name="chattingrooms",
    )

    def __str__(self):
        return "Chatting Room"


class Dm(CommonModel):
    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="directmessages",
    )

    room = models.ForeignKey(
        "dms.ChattingRoom",
        on_delete=models.CASCADE,
        related_name="directmessages",
    )

    def __str__(self):
        return f"{self.user} says : {self.text}"
