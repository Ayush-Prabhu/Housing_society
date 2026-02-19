from rest_framework import status
from .base import BaseAPITestCase
from api.models import Society


class SocietyAPITests(BaseAPITestCase):

    def test_get_societies(self):
        response = self.client.get("/api/societies/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_society(self):
        payload = {
            "name": "Blue Valley",
            "address": "Baner",
            "city": "Pune",
            "pincode": "411045"
        }

        response = self.client.post("/api/societies/", payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Society.objects.count(), 2)
