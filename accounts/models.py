from django.db import models

from django.conf import settings


class WorkerProfile(models.Model):
  user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
  employee_id = models.CharField(max_length=50, unique=True)
  full_name = models.CharField(max_length=100)

  def __str__(self):
      return self.full_name