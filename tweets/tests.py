from rest_framework.test import APITestCase
from .models import Tweet
from users.models import User


class TestTweets(APITestCase):

    def setUp(self):
        user = User.objects.create(
            username="test",
        )
        user.set_password("123")
        user.save()
        self.user = user

        Tweet.objects.create(
            user=user,
            payload="test.py TEST",
        )

    def test_all_tweets(self):
        response = self.client.get("/api/v1/tweets/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_tweet(self):
        response = self.client.post("/api/v1/tweets/", {"payload": "hihi"})
        self.assertEqual(response.status_code, 403)

        self.client.force_login(
            self.user,
        )

        response = self.client.post("/api/v1/tweets/", {"payload": "hihi"})
        self.assertEqual(response.status_code, 200)


class TestTweet(APITestCase):
    def setUp(self):
        user = User.objects.create(
            username="test",
        )
        user.set_password("123")
        user.save()
        self.user = user

        Tweet.objects.create(
            user=user,
            payload="test.py TEST",
        )

    def test_tweet_not_found(self):
        response = self.client.get("/api/v1/tweets/2")
        self.assertEqual(response.status_code, 404)

    def test_get_tweet(self):
        response = self.client.get("/api/v1/tweets/1")
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200",
        )

    def test_update_tweet(self):
        self.client.force_login(
            self.user,
        )
        response = self.client.put("/api/v1/tweets/1", {"payload": "byebye"})
        self.assertEqual(response.status_code, 200)
        self.client.logout()
        user = User.objects.create(
            username="test2",
        )
        user.set_password("123")
        user.save()
        self.client.force_login(
            user,
        )

        response = self.client.put("/api/v1/tweets/1", {"payload": "byebyebye"})
        self.assertEqual(response.status_code, 403)

    def test_delete_tweet(self):
        user = User.objects.create(
            username="test2",
        )
        user.set_password("123")
        user.save()
        self.client.force_login(
            user,
        )
        response = self.client.delete("/api/v1/tweets/1")

        self.client.logout()

        self.assertEqual(response.status_code, 403)
        self.client.force_login(
            self.user,
        )
        response = self.client.delete("/api/v1/tweets/1")
        self.assertEqual(response.status_code, 204)
