from django.db import models


class CommonModel(models.Model):
    """Common Model Definition"""

    created_at = models.DateTimeField(
        auto_now_add=True,
    )  # 생성될 때 한 번만 기록
    updated_at = models.DateTimeField(
        auto_now=True,
    )  # 수정시마다 기록

    class Meta:
        abstract = True
