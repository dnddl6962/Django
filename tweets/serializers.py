from rest_framework import serializers
from users.models import User
from .models import Tweet


class TweetSerializer(serializers.Serializer):

    pk = serializers.IntegerField(
        read_only=True,
    )
    payload = serializers.CharField(
        required=True,
        max_length=80,
    )
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field="username",
    )
    created_at = serializers.DateTimeField(
        read_only=True,
    )

    def create(self, validated_data):
        return Tweet.objects.create(
            **validated_data  # 딕셔너리를 가져와서 사용가능하게 바꿔줌
        )

    def update(self, instance, validated_data):
        instance.payload = validated_data.get("payload", instance.payload)
        instance.user = validated_data.get("user", instance.user)
        instance.save()
        return instance
