from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from .models import Employee


class RoleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        employee: Employee = request.user
        role: str = employee.role

        return Response(role)
