from employee_app.models import Employee, Role

def create_test_employee(
    role: Role,
    username: str = "user",
    name: str = "user",
    email: str = "user@email.com",
    password: str = "user"
) -> Employee :
    employee: Employee = Employee.objects.create(
        username=username,
        name=name,
        email=email,
        role=role,
        plain_password=password
    )
    employee.set_password(password)
    employee.save()
    return employee

TEST_EMPLOYEE_DATA: list[dict] = [
    {
        "username": "user1",
        "name": "user1",
        "email": "user1@email.com",
        "role": Role.SALES,
        "password": "user1"
    },
    {
        "username": "user2",
        "name": "user2",
        "email": "user2@email.com",
        "role": Role.PROCUREMENT,
        "password": "user2"
    },
    {
        "username": "user3",
        "name": "user3",
        "email": "user3@email.com",
        "role": Role.HR,
        "password": "user3"
    }
]

def create_list_test_employee(employee_data=TEST_EMPLOYEE_DATA) -> list[Employee]:
    employees: list[Employee] = []
    for employee_datum in employee_data:
        employee: Employee = create_test_employee(**employee_datum)
        employees.append(employee)
    return employees