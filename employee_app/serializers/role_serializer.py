from rest_framework import serializers
from ..models import Employee


class RoleSerializer(serializers.ModelSerializer):
    role: serializers.CharField = serializers.CharField(
        source="get_role_display"
    )

    class Meta:
        model: type[Employee] = Employee
        fields: list[str] = ["role"]
