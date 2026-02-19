from rest_framework import status
from .base import BaseAPITestCase
from api.models import Resident


class ResidentAPITests(BaseAPITestCase):

    def test_get_residents(self):
        response = self.client.get("/api/residents/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_resident(self):
        payload = {
            "society": self.society.id,
            "name": "Anita",
            "email": "anita@test.com",
            "phone_number": "+919888888888",
            "is_active": True
        }

        response = self.client.post("/api/residents/", payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Resident.objects.count(), 2)
