from rest_framework import status
from .base import BaseAPITestCase
from api.models import ServiceRequest, RequestStatus


class ServiceRequestAPITests(BaseAPITestCase):

    def test_create_service_request(self):
        payload = {
            "resident": self.resident.id,
            "request_type": "Plumbing",
            "title": "Leaking pipe",
            "description": "Kitchen pipe leaking"
        }

        response = self.client.post("/api/servicerequests/", payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ServiceRequest.objects.count(), 1)

    def test_close_service_request(self):
        request = ServiceRequest.objects.create(
            resident=self.resident,
            title="Fan not working",
            description="Bedroom fan issue"
        )
        # print(request.id)
        response = self.client.put(
            f"/api/servicerequests/{request.id}/",
            {
                "resident": self.resident.id,
                "title": request.title,
                "description": request.description,
                "status": RequestStatus.CLOSED
            },
            format="json"
        )


        request.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(request.closed)
