from django.utils import timezone
from ..models import ServiceRequest, RequestStatus
from ..serializers import ServiceRequestSerializer


def list_requests():
    return ServiceRequest.objects.all()


def get_request(pk):
    return ServiceRequest.objects.get(pk=pk)


def create_request(data):
    serializer = ServiceRequestSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()


def update_request(instance, data):
    serializer = ServiceRequestSerializer(instance, data=data)
    serializer.is_valid(raise_exception=True)
    request = serializer.save()

    if request.status == RequestStatus.CLOSED and request.closed is None:
        request.closed = timezone.now()
        request.save(update_fields=["closed"])

    return request
