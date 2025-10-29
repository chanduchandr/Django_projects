
from rest_framework import serializers
from .models import Users, Role, UserRoleMap

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class UserRoleMapSerializer(serializers.ModelSerializer):
    UserID = UsersSerializer(read_only=True)
    RoleID = RoleSerializer(read_only=True)

    class Meta:
        model = UserRoleMap
        fields = '__all__'

