from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers

from monedas.models import Moneda, MonedaUsuario, Transferencia


class MonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moneda
        fields = ['id', 'nombre', 'codigo']


class MonedaUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonedaUsuario
        fields = ['id', 'moneda', 'usuario', 'cantidad']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class BalanceSerializer(serializers.ModelSerializer):
    moneda = MonedaSerializer()
    usuario = UserSerializer()

    class Meta:
        model = MonedaUsuario
        fields = ['moneda', 'cantidad', 'usuario']


class TransferBalanceSerializer(serializers.Serializer):
    usuario_destino = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    moneda = serializers.IntegerField()
    cantidad = serializers.IntegerField()


class TransferenciaSerializer(serializers.ModelSerializer):
    usuario_origen = UserSerializer()
    usuario_destino = UserSerializer()
    moneda = MonedaSerializer()

    class Meta:
        model = Transferencia
        fields = ['id', 'usuario_origen', 'usuario_destino', 'moneda', 'cantidad']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Credenciales incorrectas")
