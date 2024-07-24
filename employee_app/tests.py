from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.response import Response
from .models import Role, Employee
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from tests.data.employee import create_list_test_employee


class LoginTest(TestCase):
    client: APIClient
    employees: list[Employee]

    def setUp(self) -> None:
        self.client = APIClient()
        self.employees = create_list_test_employee()

    def test_login(self) -> None:
        for employee in self.employees:
            token: Token = Token.objects.create(user=employee)
            expected_response: dict = {
                "token": token.key,
                "role": employee.role.label
                }

            actual_response: Response = self.client.post("/employees/login/", {
                "username": employee.username,
                "password": employee.plain_password
            })
            self.assertEqual(actual_response.status_code, 200)
            self.assertEqual(actual_response.json(), expected_response)

class EmployeeTest(TestCase):
    client: APIClient

    def setup(self) -> None:
        self.client = APIClient()

    def test_create_employee(self) -> None:
        request_body: dict = {
            "username": "user",
            "name": "user",
            "email": "user@email.com",
            "role": Role.SALES
        }

        response: Response = self.client.post("/employees/", request_body)

        self.assertEqual(response.status_code, 201)
        self.assertNotEqual(response.json(), "")

