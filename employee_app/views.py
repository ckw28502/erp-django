from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from .models import Employee
from .serializers.role_serializer import RoleSerializer


class RoleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        employee: Employee = request.user
        serializer: RoleSerializer = RoleSerializer(instance=employee)
        return Response(serializer.data)
