from rest_framework.serializers import ModelSerializer
from .models import Review
from users.serializers import UserListSerializer


class ReviewSerializer(ModelSerializer):

    user = UserListSerializer(read_only=True)

    class Meta:
        model = Review
        fields = (
            "user",
            "payload",
            "rating",
        )
