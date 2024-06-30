from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RoleView

urlpatterns = [
    path("login/", obtain_auth_token, name="login"),
    path("role/", RoleView.as_view(), name="role")
]
