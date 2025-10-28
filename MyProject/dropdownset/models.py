from django.db import models
from commonapp.models import Common
import uuid


class DropDownSet(Common):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    DropDownGroup = models.CharField(max_length=100)
    DropDownValue = models.CharField(max_length=100)
    DropDownShortName = models.CharField(max_length=20)
