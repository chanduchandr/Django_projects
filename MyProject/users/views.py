from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UsersSerializer, RoleSerializer, UserRoleMapSerializer
from .models import Users, Role, UserRoleMap

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('FirstName')
    serializer_class = UsersSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by('RoleName')
    serializer_class = RoleSerializer

class UserRoleMapViewSet(viewsets.ModelViewSet):
    queryset = UserRoleMap.objects.all()
    serializer_class = UserRoleMapSerializer


