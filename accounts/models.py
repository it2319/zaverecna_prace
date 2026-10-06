from django.db import models


class WorkerRole(models.TextChoices):
    WORKER = "worker", "Worker"
    ADMIN = "admin", "Admin"


class WorkerProfile(models.Model):
  user_id = models.UUIDField(unique=True)
  employee_id = models.CharField(max_length=50, unique=True)
  full_name = models.CharField(max_length=100)
  role = models.CharField(
    max_length=20,
    choices=WorkerRole.choices,
    default=WorkerRole.WORKER
    )
  is_active = models.BooleanField(default=True)

