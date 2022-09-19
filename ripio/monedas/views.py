from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, views, status, mixins
from rest_framework.authentication import get_authorization_header
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken

JWT_authenticator = JWTAuthentication()

from monedas.models import Moneda, MonedaUsuario, Transferencia
from monedas.permissions import BasicUserPermission
from monedas.serializers import BalanceSerializer, MonedaSerializer, MonedaUsuarioSerializer, UserSerializer, \
    TransferBalanceSerializer, TransferenciaSerializer
from monedas.services import MonedaTransferService


class MonedaViewSet(viewsets.ModelViewSet):
    queryset = Moneda.objects.all()
    serializer_class = MonedaSerializer
    permission_classes = (AllowAny,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializers = {
        'default': UserSerializer,
        'get_balances_for_user': BalanceSerializer,
        'transfer_to_user': TransferBalanceSerializer
    }
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        return self.serializers.get(
            self.action, self.serializers["default"])

    # @action(detail=True, methods=["get"])
    # def get_balances_for_user(self, request, pk=None):
    #     user = self.get_object()
    #     queryset = MonedaUsuario.objects.filter(usuario=user)
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    @action(detail=False, methods=["post"])
    def transfer_to_user(self, request, pk=None):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        with transaction.atomic():
            balance = MonedaTransferService.transfer(user, data)
            return Response(f"Transferiste con exito {data['cantidad']} {balance.moneda.nombre}",
                            status=status.HTTP_200_OK)


class MonedaUsuarioViewSet(viewsets.ModelViewSet):
    queryset = MonedaUsuario.objects.all()
    serializers = {
        'default': MonedaUsuarioSerializer,
        'list': BalanceSerializer,
    }
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('usuario', 'moneda')
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        return self.serializers.get(
            self.action, self.serializers["default"])


class TransferenciaViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Transferencia.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TransferenciaSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('usuario_origen', 'usuario_destino', 'moneda')


@api_view(['GET'])
@permission_classes([AllowAny])
def validate_token(request):
    try:
        JWT_authenticator.get_validated_token(get_authorization_header(request).decode('utf-8').split(' ')[1])
        return Response(status=status.HTTP_200_OK)
    except InvalidToken:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

# class LoginView(views.APIView):
#     permission_classes = (AllowAny,)
#
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         login(request, user)
#         return Response(status=status.HTTP_202_ACCEPTED)
#
#
# class LogoutView(views.APIView):
#     permission_classes = (AllowAny,)
#
#     def get(self, request):
#         if request.user.is_authenticated:
#             logout(request)
#         return Response(status=status.HTTP_202_ACCEPTED)
