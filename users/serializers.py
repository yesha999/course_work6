from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
# Здесь нам придется переопределить сериалайзер, который использует djoser
# для создания пользователя из за того, что у нас имеются нестандартные поля


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    pass


class CurrentUserSerializer(serializers.ModelSerializer):
    pass
