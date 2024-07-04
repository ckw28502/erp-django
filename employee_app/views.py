from rest_framework.response import Response
from rest_framework.request import Request
from .models import Employee
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class LoginView(ObtainAuthToken):
    def post(self, request: Request):
        serializer = self.serializer_class(
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
