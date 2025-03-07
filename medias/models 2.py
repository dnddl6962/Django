from django.db import models
from common.models import CommonModel


class Photo(CommonModel):
    """Photo Model Definition"""

    file = models.ImageField()
    descprition = models.CharField(
        max_length=140,
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="medias",
    )

    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="medias",
    )

    def __str__(self):
        return f"Photo file"


class Video(CommonModel):
    file = models.FileField()
    experience = models.OneToOneField(
        "experiences.Experience",
        on_delete=models.CASCADE,
        related_name="Videos",
    )

    def __str__(self):
        return f"Video file"
