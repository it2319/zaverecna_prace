from django.db import models
from django.utils import timezone
from accounts.models import WorkerProfile
import secrets


def generate_qr_token():
    return secrets.token_urlsafe(32)

class machineStatus(models.TextChoices):
    ACTIVE = "active", "Active"
    MAINTENANCE = "maintenance", "Maintenance"
    INACTIVE = "inactive", "Inactive"

class jobStatus(models.TextChoices):
    PLANNED = "planned", "Planned"
    AVAILABLE = "available", "Available"
    ACTIVE = "active", "Active"
    COMPLETED = "completed", "Completed"
    CANCELLED = "cancelled", "Cancelled"

class Status(models.TextChoices):
    START = "start", "Start"
    END = "end", "End"
    BREAK = "break", "Break"

class Machine(models.Model): 
  name = models.CharField(max_length=100)
  code = models.CharField (max_length=50, unique=True)
  description = models.TextField (blank=True)
  qr_token = models.CharField (unique=True, max_length=255,editable=False, default=generate_qr_token)
  status = models.CharField(
        max_length=20,
        choices=machineStatus.choices,
        default=machineStatus.ACTIVE,
    )
  def __str__(self):
      return f"{self.name} - {self.code}"

class Job(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField (blank=True)
    required_quantity = models.PositiveIntegerField (null=True, blank=True)
    deadline = models.DateField (null=True, blank=True)
    note = models.TextField (blank=True)
    status = models.CharField(
        max_length=20,
        choices=jobStatus.choices,
        default=jobStatus.AVAILABLE,
    )
    def __str__(self):
        return self.name
  
class Time(models.Model):
  worker = models.ForeignKey(WorkerProfile, on_delete=models.PROTECT)
  machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
  job = models.ForeignKey(Job, on_delete=models.PROTECT)
  status = models.CharField(
    max_length=20,
    choices=Status.choices,
    default=Status.START
  )
  timestamp = models.DateTimeField(default=timezone.now)
