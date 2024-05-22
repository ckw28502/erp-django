from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

class Role(models.TextChoices):
    SALES = "Sales", "Sales"
    PROCUREMENT = "Procurement", "Procurement"
    HR = "HR", "Human Resource"

class Employee(AbstractBaseUser):
    username = models.CharField(unique=True)
    name = models.CharField()
    email = models.CharField()
    role = models.CharField(choices=Role.choices)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

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

