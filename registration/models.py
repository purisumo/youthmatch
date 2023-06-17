from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import JobType
# Create your models here.

class User(AbstractUser):
    skills = models.ManyToManyField(JobType, default=None)
    photo = models.ImageField(upload_to='Profile', default=None)
    exp = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    education = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username