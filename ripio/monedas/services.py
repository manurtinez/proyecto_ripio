from rest_framework.exceptions import NotFound, ValidationError

from monedas.models import MonedaUsuario, Transferencia


def get_moneda_usuario(moneda, usuario):
    try:
        return MonedaUsuario.objects.get(moneda=moneda, usuario=usuario)
    except MonedaUsuario.DoesNotExist:
        raise NotFound(detail="No existe la moneda para el usuario")


class MonedaTransferService:
    @staticmethod
    def transfer(usuario_origen, data):
        if usuario_origen.pk == data['usuario_destino']:
            raise ValidationError(detail="No se puede transferir a si mismo")

        balance_usuario_origen = get_moneda_usuario(data['moneda'], usuario_origen)
        balance_usuario_destino = get_moneda_usuario(data['moneda'], data['usuario_destino'])
        balance_usuario_origen.restar_balance(data['cantidad'])
        balance_usuario_destino.sumar_balance(data['cantidad'])

        Transferencia.objects.create(
            usuario_origen=usuario_origen,
            usuario_destino=balance_usuario_destino.usuario,
            moneda=balance_usuario_origen.moneda,
            cantidad=data['cantidad']
        )

        return balance_usuario_origen
