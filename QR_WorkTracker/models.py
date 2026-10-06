from enum import unique

from django.db import models

from accounts.models import WorkerProfile

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

class sessionStatus(models.TextChoices):
    ACTIVE = "active", "Active"
    COMPLETED = "completed", "Completed"
    CANCELLED = "cancelled", "Cancelled"

class pauseReason(models.TextChoices):
    BREAK = "break", "Break"
    MAINTENANCE = "maintenance", "Maintenance"
    OTHER = "other", "Other"

class Machine(models.Model): 
  name = models.CharField(max_length=100)
  code = models.CharField (max_length=50, unique=True)
  description = models.TextField (blank=True, null=True)
  qr_token = models.CharField (unique=True, max_length=255)
  status = models.CharField(
        max_length=20,
        choices=machineStatus.choices,
        default=machineStatus.ACTIVE,
    )

class Job(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField (null=True, blank=True)
    required_quantity = models.PositiveIntegerField (null=True, blank=True)
    deadline = models.DateField (null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=jobStatus.choices,
        default=jobStatus.AVAILABLE,
    )

class Job_Machine(models.Model):
        job = models.ForeignKey(Job, on_delete=models.PROTECT)
        machine = models.ForeignKey(Machine, on_delete=models.PROTECT)

        class Meta:
          constraints = [
            models.UniqueConstraint(
            fields=["job", "machine"],
            name="unique_job_machine",
            ) 
          ]

class WorkSession(models.Model):
  worker = models.ForeignKey(WorkerProfile, on_delete=models.PROTECT)
  machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
  job = models.ForeignKey(Job, on_delete=models.PROTECT)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField (null=True, blank=True)
  status = models.CharField(
    max_length=20,
    choices=sessionStatus.choices,
    default=sessionStatus.ACTIVE
  )
  
class Pause(models.Model):
  work_session = models.ForeignKey(WorkSession, on_delete=models.CASCADE)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField (null=True,blank=True)
  reason = models.CharField(
    max_length=20,
    choices=pauseReason.choices,
    default=pauseReason.BREAK
  )
  explanation = models.TextField (blank=True)

