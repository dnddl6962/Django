from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Experience, Perk
from categories.serializers import CategorySerializer
from medias.serializers import PhotoSerializer


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"


class ExperienceSerializer(ModelSerializer):

    category = CategorySerializer(read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "category",
            "photos",
            "is_owner",
        )

    def get_is_owner(self, experience):
        request = self.context["request"]
        return experience.host == request.user


class ExperienceDetailSerializer(ModelSerializer):

    category = CategorySerializer(read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = "__all__"

    def get_is_owner(self, experience):
        request = self.context["request"]
        return experience.host == request.user
