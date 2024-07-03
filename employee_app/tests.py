from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.response import Response
from .models import Role, Employee
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


class RoleViewTest(TestCase):
    client: APIClient
    username: str
    password: str
    roles: list[Role]

    def setUp(self) -> None:
        self.client = APIClient()
        self.username = "user"
        self.password = "user"
        self.roles = [Role.SALES, Role.PROCUREMENT, Role.HR]

    def test_unauthenticated(self) -> None:
        response: Response = self.client.get("/employees/role/")

        self.assertEqual(response.status_code, 401)

    def test_get_role(self) -> None:
        for i in range(len(self.roles)):
            role: Role = self.roles[i]
            employee: Employee = get_user_model().objects.create_user(
                username=f"{self.username}{i}",
                email=f"{self.username}{i}@email.com",
                password=self.password,
                role=role
            )
            token: Token = Token.objects.create(user=employee)
            self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
            expected_response: dict = {"role": role.label}

            actual_response: Response = self.client.get("/employees/role/")

            self.assertEqual(actual_response.status_code, 200)
            self.assertEqual(expected_response, actual_response.json())
