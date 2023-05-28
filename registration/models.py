from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import JobType
# Create your models here.

class User(AbstractUser):
    skills = models.ManyToManyField(JobType)

    def __str__(self):
        return self.username