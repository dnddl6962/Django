from django.shortcuts import render
from .models import Tweet

# Create your views here.


# request = 누가 요청했는지, 어떤 데이터가 전송되고 있는지?
def see_all_tweets(request):
    tweets = Tweet.objects.all()
    return render(
        request,
        "all_tweets.html",
        {
            "tweets": tweets,
        },
    )


def see_one_tweet(request, tweet_pk):
    try:
        tweet = Tweet.objects.get(pk=tweet_pk)
        return render(
            request,
            "one_tweet.html",
            {"tweet": tweet},
        )
    except Tweet.DoesNotExist:
        return render(
            request,
            "one_tweet.html",
            {
                "not_found": True,
            },
        )
