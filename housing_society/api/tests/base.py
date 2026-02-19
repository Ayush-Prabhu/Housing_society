# tests/base.py
from rest_framework.test import APITestCase
from django.urls import reverse
from api.models import Society, Resident


class BaseAPITestCase(APITestCase):
    def setUp(self):
        self.society = Society.objects.create(
            name="Green Meadows",
            address="MG Road",
            city="Pune",
            pincode="411001"
        )

        self.resident = Resident.objects.create(
            society=self.society,
            name="Rahul",
            email="rahul@test.com",
            phone_number="+919999999999",
            is_active=True
        )
