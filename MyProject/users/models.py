from django.db import models
from commonapp.models import Common
import uuid



class Users(Common):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=20)
    Email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.Id}"


class Role(Common):
    Id = models.BigAutoField(primary_key=True)
    RoleName = models.CharField(max_length=100)

    def __str__(self):
        return self.RoleName


class UserRoleMap(Common):
    Id = models.BigAutoField(primary_key=True)
    UserID = models.ForeignKey(Users, on_delete=models.CASCADE)
    RoleID = models.ForeignKey(Role, on_delete=models.CASCADE)