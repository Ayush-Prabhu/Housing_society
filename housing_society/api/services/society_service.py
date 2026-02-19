from ..models import Society
from ..serializers import SocietySerializer


def list_societies():
    return Society.objects.all()


def get_society(pk):
    return Society.objects.get(pk=pk)


def create_society(data):
    serializer = SocietySerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()


def update_society(instance, data):
    serializer = SocietySerializer(instance, data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
