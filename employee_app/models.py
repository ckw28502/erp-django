from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


class Role(models.TextChoices):
    SALES = "Sales", "Sales"
    PROCUREMENT = "Procurement", "Procurement"
    HR = "HR", "Human Resource"


class Employee(AbstractBaseUser):
    username: str = models.CharField(unique=True)
    name: str = models.CharField()
    email: str = models.CharField(unique=True)
    role: str = models.CharField(choices=Role.choices)

    is_active: bool = models.BooleanField(default=True)
    is_staff: bool = models.BooleanField(default=False)
    is_admin: bool = models.BooleanField(default=False)
    is_superuser: bool = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="employee_set",
        blank=True
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="employee_set",
        blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name", "role"]
