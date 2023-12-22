from typing import Any
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest

class CustomBackend(ModelBackend):
    def authenticate(self, request: HttpRequest, username: str | None = ..., password: str | None = ..., **kwargs: Any) -> AbstractBaseUser | None:
        user=self.custom_auth(username,password)
        if user is not None:
            return user
        return None

    def custom_auth(self,username,password):
        user_mode=get_user_model()
        print(user_mode)
        user=user_mode.objects.get(username=username)
        if user.check_password(password):
            return user
        return None