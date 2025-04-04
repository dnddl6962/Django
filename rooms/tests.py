from rest_framework.test import APITestCase
from . import models
from users.models import User


class TestAmenities(APITestCase):

    NAME = "Amenity Test"
    DESCRIPTION = "Amenity Description Test"
    URL = "/api/v1/rooms/amenities"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESCRIPTION,
        )

    def test_all_amenities(self):

        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200",
        )
        self.assertIsInstance(
            data,
            list,
        )
        self.assertEqual(
            len(data),
            1,
        )
        self.assertEqual(
            data[0]["name"],
            self.NAME,
        )
        self.assertEqual(
            data[0]["description"],
            self.DESCRIPTION,
        )

    def test_create_amenity(self):

        new_name = "New Amenity"
        new_desc = "New Amenity Description"

        response = self.client.post(
            self.URL,
            data={"name": new_name, "description": new_desc},
        )

        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["name"], new_name, "wrong name")
        self.assertEqual(data["description"], new_desc, "wrong desc")

        response2 = self.client.post(self.URL, data={"description": "test"})

        self.assertEqual(response2.status_code, 400)


class TestAmenity(APITestCase):

    NAME = "Test Amenity"
    DESC = "Test Dsc"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_amenity_not_found(self):
        response = self.client.get("/api/v1/rooms/amenities/2")

        self.assertEqual(response.status_code, 404)

    def test_get_amenity(self):

        response = self.client.get("/api/v1/rooms/amenities/1")

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(
            data["name"],
            self.NAME,
        )
        self.assertEqual(
            data["description"],
            self.DESC,
        )

    def test_put_amenity(self):
        pass

    def test_delete_amenity(self):

        response = self.client.delete("/api/v1/rooms/amenities/1")

        self.assertEqual(response.status_code, 204)


class TestRooms(APITestCase):

    def setUp(self):
        user = User.objects.create(
            username="test",
        )
        user.set_password("123")
        user.save()
        self.user = user

    def test_create_room(self):

        response = self.client.post("/api/v1/rooms/")

        self.assertEqual(response.status_code, 403)

        self.client.force_login(
            self.user,
        )
