from rest_framework.response import Response
from rest_framework.request import Request
from .models import Employee
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from rest_framework import status


class LoginView(ObtainAuthToken):
    def post(self, request: Request) -> Response:
        serializer: Serializer = self.serializer_class(
            data=request.data,
            context={"request": request}
            )
        serializer.is_valid(raise_exception=True)
        employee: Employee = serializer.validated_data["user"]
        token: Token = Token.objects.get_or_create(user=employee)[0]
        return Response({
            "token": token.key,
            "role": employee.get_role_display()
        })

class EmployeeView(APIView):
    def post(self, request: Request) -> Response:
        serializer: Serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            response_body: dict = serializer.save()
            return Response(response_body, status=status.HTTP_201_CREATED)
