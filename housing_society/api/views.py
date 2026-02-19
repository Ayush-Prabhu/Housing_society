from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Society, Resident, ServiceRequest
from .serializers import SocietySerializer, ResidentSerializer, ServiceRequestSerializer

from .services.society_service import (
    list_societies, get_society, create_society, update_society
)
from .services.resident_service import (
    list_residents, get_resident, create_resident, update_resident
)
from .services.request_service import (
    list_requests, get_request, create_request, update_request
)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/societies',
        'GET /api/societies/<int:id>',
        'GET /api/residents',
        'GET /api/residents/<int:id>',
        'GET /api/societies/<int:id>/residents',
        'GET /api/servicerequests',
        'GET /api/servicerequests/<int:id>',
        'GET /api/residents/<int:id>/servicerequests',
        'POST /api/societies',
        'POST /api/residents',
        'POST /api/servicerequests',
        'PUT /api/societies/<int:id>',
        'PUT /api/residents/<int:id>',
        'PUT /api/servicerequests/<int:id>',
        'DELETE /api/societies/<int:id>',
        'DELETE /api/residents/<int:id>',
        'DELETE /api/servicerequests/<int:id>',
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def societiesList(request):
    if request.method == 'GET':
        societies = list_societies()
        return Response(SocietySerializer(societies, many=True).data)

    society = create_society(request.data)
    return Response(SocietySerializer(society).data, status=201)


@api_view(['GET', 'POST'])
def residentsList(request):
    if request.method == 'GET':
        residents = list_residents()
        return Response(ResidentSerializer(residents, many=True).data)

    resident = create_resident(request.data)
    return Response(ResidentSerializer(resident).data, status=201)


@api_view(['GET', 'POST'])
def serviceRequestsList(request):
    if request.method == 'GET':
        requests = list_requests()
        return Response(ServiceRequestSerializer(requests, many=True).data)

    request_obj = create_request(request.data)
    return Response(ServiceRequestSerializer(request_obj).data, status=201)


@api_view(['GET', 'PUT', 'DELETE'])
def societiesDetail(request, pk):
    try:
        society = get_society(pk)
    except Society.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        return Response(SocietySerializer(society).data)

    if request.method == 'PUT':
        society = update_society(society, request.data)
        return Response(SocietySerializer(society).data)

    society.delete()
    return Response(status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def residentsDetail(request, pk):
    try:
        resident = get_resident(pk)
    except Resident.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        return Response(ResidentSerializer(resident).data)

    if request.method == 'PUT':
        resident = update_resident(resident, request.data)
        return Response(ResidentSerializer(resident).data)

    resident.delete()
    return Response(status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def serviceRequestsDetail(request, pk):
    try:
        request_obj = get_request(pk)
    except ServiceRequest.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        return Response(ServiceRequestSerializer(request_obj).data)

    if request.method == 'PUT':
        request_obj = update_request(request_obj, request.data)
        return Response(ServiceRequestSerializer(request_obj).data)

    request_obj.delete()
    return Response(status=204)


@api_view(['GET'])
def societyResidentsDetail(request, pk):
    try:
        society = Society.objects.get(pk=pk)
    except Society.DoesNotExist:
        return Response(status=404)

    residents = Resident.objects.filter(society=society)
    return Response(ResidentSerializer(residents, many=True).data)


@api_view(['GET'])
def residentRequestsDetail(request, pk):
    try:
        resident = Resident.objects.get(pk=pk)
    except Resident.DoesNotExist:
        return Response(status=404)

    requests = ServiceRequest.objects.filter(resident=resident)
    return Response(ServiceRequestSerializer(requests, many=True).data)
