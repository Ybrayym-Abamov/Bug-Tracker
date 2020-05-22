from django.db import models
from django.contrib.auth.models import AbstractUser


class Ticket(models.Model):
    pass


class MyUser(AbstractUser):
    pass
