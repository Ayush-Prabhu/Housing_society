from ..models import Resident
from ..serializers import ResidentSerializer


def list_residents():
    return Resident.objects.all()


def get_resident(pk):
    return Resident.objects.get(pk=pk)


def create_resident(data):
    serializer = ResidentSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()


def update_resident(instance, data):
    serializer = ResidentSerializer(instance, data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
