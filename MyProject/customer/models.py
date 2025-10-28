from django.db import models
from commonapp.models import Common
import uuid


class Customer(Common):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"
