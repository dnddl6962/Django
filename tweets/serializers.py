# from rest_framework.ser import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import User
from .models import Tweet


class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "avatar",
            "username",
        )


class TweetsSerializer(ModelSerializer):
    user = TinyUserSerializer(read_only=True)
    total_likes = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = (
            "pk",
            "payload",
            "user",
            "total_likes",
        )

    def get_total_likes(self, tweet):
        return tweet.total_likes()


class TweetSerializer(ModelSerializer):

    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = "__all__"


# class TweetSerializer(serializers.Serializer):

#     pk = serializers.IntegerField(
#         read_only=True,
#     )
#     payload = serializers.CharField(
#         required=True,
#         max_length=80,
#     )
#     user = serializers.SlugRelatedField(
#         queryset=User.objects.all(),
#         slug_field="username",
#     )
#     created_at = serializers.DateTimeField(
#         read_only=True,
#     )

#     def create(self, validated_data):
#         return Tweet.objects.create(
#             **validated_data  # 딕셔너리를 가져와서 사용가능하게 바꿔줌
#         )

#     def update(self, instance, validated_data):
#         instance.payload = validated_data.get("payload", instance.payload)
#         instance.user = validated_data.get("user", instance.user)
#         instance.save()
#         return instance
