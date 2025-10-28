from django.db import models
from commonapp.models import Common
import uuid

class Region(Common):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    RegionName = models.CharField(max_length=100)

    def __str__(self):
        return self.RegionName
    

class Property(Common):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    PropertieName = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    ZipCode = models.CharField(max_length=20)
    RegionID = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    PropertyType = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=18, decimal_places=2)
    BedRoom = models.IntegerField()
    BathRooms = models.IntegerField()
    SizeInSqft = models.DecimalField(max_digits=18, decimal_places=2)
    IsDisplay = models.BooleanField(default=True)

    def __str__(self):
        return self.PropertieName
