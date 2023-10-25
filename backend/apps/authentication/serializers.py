from django.contrib.auth.models import User
from rest_framework import serializers
from apps.authentication.models import Account
from apps.authentication.models import Contatos

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop("password")
        email = validated_data.pop("username")
        user = User(username=email)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ("pk", "username", "password")


class AccountSerializer(serializers.ModelSerializer):
      class Meta:
        model = Account
        fields = '__all__'

class ContatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contatos
        fields = '__all__'