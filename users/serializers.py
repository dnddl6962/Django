from rest_framework.serializers import ModelSerializer
from .models import User
from rooms.models import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
        )


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "date_joined",
            "avatar",
        )


class UserDetailSerializer(ModelSerializer):

    rooms = RoomSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "date_joined",
            "avatar",
            "rooms",
        )


class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "is_staff",
            "is_active",
            "id",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )
