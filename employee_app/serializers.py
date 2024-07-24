from rest_framework import serializers
from .models import Employee
from django.utils.crypto import get_random_string

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model: Employee = Employee
        fields: list[str] = ["username", "name", "email", "role"]
        extra_kwargs: dict = {"password": {"write_only": True}}

    def create(self, validated_data) -> dict:
        password: str = get_random_string(length=12)

        employee: Employee = Employee.objects.create(
            username=validated_data["username"],
            name=validated_data["name"],
            email=validated_data["email"],
            role=validated_data["role"]
        )

        employee.set_password(password)
        employee.save()

        return {"password": password}