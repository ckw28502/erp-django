from django.urls import path
from .views import LoginView, EmployeeView

urlpatterns = [
    path("", EmployeeView.as_view(), name="employee"),
    path("login/", LoginView.as_view(), name="login")
]
