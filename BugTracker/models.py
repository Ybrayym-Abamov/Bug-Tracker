from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from TheBTProject.settings import AUTH_USER_MODEL


#  REFERENCES:
#  https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices
#  https://docs.djangoproject.com/en/3.0/ref/models/fields/


class Ticket(models.Model):
    title = models.CharField(max_length=30, default=None)
    datetime = models.DateTimeField(default=timezone.now)
    description = models.TextField(default=None)
    ticketfiler = models.ForeignKey(
        AUTH_USER_MODEL, related_name='ticketfiler',
        on_delete=models.CASCADE, default=None)
    NEW = "N"
    INPROGRESS = "InP"
    DONE = "D"
    INVALID = "InV"
    TICKET_STATUS_CHOICES = [
        (NEW, 'New'),
        (INPROGRESS, 'Inprogress'),
        (DONE, 'Done'),
        (INVALID, 'Invalid')
    ]
    status = models.CharField(
        max_length=3, choices=TICKET_STATUS_CHOICES, default=NEW)
    assignedto = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='assignedto',
        blank=True,
        null=True,
        default=None)
    completedby = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='completedby',
        blank=True,
        null=True,
        default=None)

#  __str__ is the built-in function in python,
#  used for string representation of object.
    def __str__(self):
        return self.title


class MyUser(AbstractUser):
    pass
