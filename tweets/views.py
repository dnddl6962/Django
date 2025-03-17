# from django.shortcuts import render
# from django.http import JsonResponse
# from django.core import serializers
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Tweet
from rest_framework.views import APIView
from users.models import User
from .serializers import TweetsSerializer, TweetSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.


class Tweets(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_tweets = Tweet.objects.all()
        serializers = TweetsSerializer(
            all_tweets,
            many=True,
        )
        return Response(serializers.data)

    def post(self, request):
        serializers = TweetsSerializer(data=request.data)
        if serializers.is_valid():
            new_tweet = serializers.save(user=request.user)
            return Response(
                TweetsSerializer(new_tweet).data,
            )
        else:
            return Response(serializers.errors)


class OneTweet(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            tweet = Tweet.objects.get(pk=pk)
            return tweet
        except Tweet.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        tweet = self.get_object(pk)
        serializers = TweetSerializer(
            tweet,
        )
        return Response(
            serializers.data,
        )

    def put(self, request, pk):

        tweet = self.get_object(pk)
        if tweet.user != request.user:
            raise PermissionDenied
        serializers = TweetSerializer(
            tweet,
            data=request.data,
            partial=True,
        )
        if serializers.is_valid():
            updated_tweet = serializers.save(user=request.user)
            return Response(TweetSerializer(updated_tweet).data)
        else:
            return Response(serializers.errors)

    def delete(self, request, pk):
        tweet = self.get_object(pk)
        if tweet.user != request.user:
            raise PermissionDenied
        tweet.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class UserTweets(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            raise NotFound

        tweets = user.tweets.all()  # related_name="tweets" 사용
        serializers = TweetSerializer(tweets, many=True)

        return Response(serializers.data)


# @api_view(["GET", "POST"])
# def tweets(request):
#     if request.method == "GET":
#         all_tweets = Tweet.objects.all()
#         serializers = TweetSerializer(
#             all_tweets,
#             many=True,
#         )
#         return Response(
#             serializers.data,
#         )
#     elif request.method == "POST":
#         serializers = TweetSerializer(
#             data=request.data,
#         )
#         if serializers.is_valid() == True:
#             new_tweet = serializers.save()
#             return Response(
#                 TweetSerializer(new_tweet).data,
#             )
#         else:
#             return Response(serializers.errors)


# @api_view(["GET", "PUT", "DELETE"])
# def tweet(request, tweet_pk):
#     try:
#         tweet = Tweet.objects.get(pk=tweet_pk)
#     except Tweet.DoesNotExist:
#         raise NotFound
#     if request.method == "GET":
#         serializers = TweetSerializer(tweet)
#         return Response(
#             serializers.data,
#         )
#     elif request.method == "PUT":
#         serializers = TweetSerializer(
#             tweet,
#             data=request.data,
#             partial=True,
#         )
#         if serializers.is_valid() == True:
#             updated_tweet = serializers.save()
#             return Response(
#                 TweetSerializer(updated_tweet).data,
#             )
#         else:
#             return Response(serializers.errors)
#     elif request.method == "DELETE":
#         tweet.delete()
#         return Response(status=HTTP_204_NO_CONTENT)


# @api_view(["GET"])
# def user_tweets(request, user_id):
#     try:
#         user = User.objects.get(id=user_id)
#     except User.DoesNotExist:
#         raise NotFound

#     tweets = user.tweets.all()  # related_name="tweets" 사용
#     serializers = TweetSerializer(tweets, many=True)

#     return Response(serializers.data)


# jsonresponse 이용
# def tweets(request):
#     all_tweets = Tweet.objects.all()
#     return JsonResponse(
#         {
#             "ok": True,
#             "tweets": serializers.serialize("json", all_tweets),
#         },
#     )


# render 이용
# def see_all_tweets(request):      # request = 누가 요청했는지, 어떤 데이터가 전송되고 있는지?
#     tweets = Tweet.objects.all()
#     return render(
#         request,
#         "all_tweets.html",
#         {
#             "tweets": tweets,
#         },
#     )


# def see_one_tweet(request, tweet_pk):
#     try:
#         tweet = Tweet.objects.get(pk=tweet_pk)
#         return render(
#             request,
#             "one_tweet.html",
#             {"tweet": tweet},
#         )
#     except Tweet.DoesNotExist:
#         return render(
#             request,
#             "one_tweet.html",
#             {
#                 "not_found": True,
#             },
#         )
