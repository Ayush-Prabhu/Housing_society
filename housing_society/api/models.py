from django.db import models
from django.core.validators import RegexValidator
import uuid


class Society(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_column='Id'
    )
    name = models.CharField(max_length=200, db_column="Name")
    address = models.TextField(max_length=300, db_column="Address")
    city = models.CharField(max_length=100, db_column="City")
    pincode = models.CharField(
        max_length=6,
        db_column="Pincode",
        validators=[
            RegexValidator(
                regex=r'^[0-9]{6}$',
                message="Pin code must be exactly 6 digits."
            )
        ]
    )
    created = models.DateTimeField(auto_now_add=True, db_column="CreatedAt")
    # updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        db_table="societies"

    def __str__(self):
        return self.name


class Resident(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_column="Id",
    )
    
    society = models.ForeignKey(
        Society,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="SocietyId"
    )
    name = models.CharField(max_length=150, db_column="FullName")
    email = models.EmailField(max_length=200, db_column="Email")
    phone_number = models.CharField(
        max_length=15,
        db_column="Phone",
        validators=[
            RegexValidator(
                regex=r'^\+?\d{9,15}$',
                message="Phone number must be in international format."
            )
        ]
    )
    flat_number = models.CharField(max_length=50, db_column="FlatNumber")
    is_active = models.BooleanField(default=True, db_column="IsActive")
    joined = models.DateTimeField(auto_now_add=True, db_column="JoinedOn")

    class Meta:
        db_table="residents"
    def __str__(self):
        return self.name


class RequestTypes(models.IntegerChoices):
    PLUMBING = 1, "Plumbing"
    ELECTRICAL = 2, "Electrical"
    SECURITY = 3, "Security"
    OTHER = 4, "Other"


class RequestStatus(models.IntegerChoices):
    OPEN = 1, "Open"
    IN_PROGRESS = 2, "In Progress"
    RESOLVED = 3, "Resolved"
    CLOSED = 4, "Closed"
    CANCELLED = 5, "Cancelled"


class ServiceRequest(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_column="Id"
    )
    
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE, db_column="ResidentId")
    request_type = models.IntegerField(
        max_length=20,
        choices=RequestTypes.choices,
        default=RequestTypes.OTHER,
        db_column="Type"
    )
    title = models.CharField(max_length=200, db_column="Title")
    description = models.TextField(max_length=2000, db_column="Description")
    status = models.IntegerField(
        max_length=20,
        choices=RequestStatus.choices,
        default=RequestStatus.OPEN,
        db_column="Status"
    )
    created = models.DateTimeField(auto_now_add=True, db_column="CreatedAt")
    updated = models.DateTimeField(auto_now=True, db_column="UpdatedAt")
    closed = models.DateTimeField(null=True, blank=True, db_column="ClosedAt")

    def __str__(self):
        return self.title
    class Meta:
        db_table="service_requests"
