from django.urls import path
from . import views
import uuid

urlpatterns = [
    path('', views.getRoutes),
    path('societies/<uuid:pk>/residents',views.societyResidentsDetail),
    path('societies/<uuid:pk>',views.societiesDetail),
    path('residents/<uuid:pk>/servicerequests',views.residentRequestsDetail),
    path('residents/<uuid:pk>',views.residentsDetail),
    path('servicerequests/<uuid:pk>',views.serviceRequestsDetail),
    path('societies/',views.societiesList),
    path('residents/',views.residentsList),
    path('servicerequests/',views.serviceRequestsList),
]