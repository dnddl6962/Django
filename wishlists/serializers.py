from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Wishlist
from rooms.serializers import RoomListSerializer


class WishlistSerializer(ModelSerializer):

    rooms = RoomListSerializer(many=True, read_only=True)

    class Meta:
        model = Wishlist
        fields = (
            "pk",
            "name",
            "rooms",
        )
