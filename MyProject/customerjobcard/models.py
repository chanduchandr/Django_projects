from django.db import models
from commonapp.models import Common
from propertyapp.models import Property
from customer.models import Customer
from users.models import Role
from propertyapp.models import Region
import uuid
# Create your models here.


class JobCard(Common):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    PropertieID = models.ForeignKey(Property, on_delete=models.CASCADE)
    CustomerClickID = models.BigIntegerField(null=True, blank=True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    StatusID = models.BigIntegerField(null=True, blank=True)
    RoleID = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    RegionID = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
