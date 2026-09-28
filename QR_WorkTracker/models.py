from enum import unique

from django.db import models

from accounts.models import WorkerProfile

class Machine(models.Model): 
  name = models.CharField(max_length=100)
  code = models.CharField (max_length=50, unique=True)
  description = models.TextField (blank=True, null=True)
  qr_token = models.CharField (unique=True, max_length=255)
  status = models.EnumField (
    choices=[
    ('active', 'Active'),
    ('maintenance', 'Maintenance'),
    ('inactive', 'Inactive')
    ], default='active')

class Job(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField (null=True, blank=True)
    required_quantity = models.TextField (null=True, blank=True)
    deadline = models.DateField (null=True, blank=True)
    status = models.EnumField (
      choices=[
      ('available', 'Available'),
      ('active', 'Active'),
      ('completed', 'Completed'),
      ('cancelled', 'Cancelled')
      ], default='available')

class Job_Machine(models.Model):
        job = models.ForeignKey(Job, on_delete=models.PROTECT)
        machine = models.ForeignKey(Machine, on_delete=models.PROTECT)

        indexes  = {
           (job, machine) (unique=True)
        }

class WorkSession(models.Model):
  worker = models.ForeignKey(WorkerProfile, on_delete=models.PROTECT)
  machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
  jpb = models.ForeignKey(Job, on_delete=models.PROTECT)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField (null=True, blank=True)
  status = models.EnumField (
    choices=[
    ('active', 'Active'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled')
    ])
  
class Pause(models.Model):
  work_session = models.ForeignKey(WorkSession, on_delete=models.CASCADE)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField (null=True,blank=True)
  reason = models.EnumField (
    choices=[
    ('break', 'Break'),
    ('maintenance', 'Maintenance'),
    ('other', 'Other')
    ])
  explanation = models.TextField (blank=True)

