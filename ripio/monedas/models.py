from django.contrib.auth.models import User
from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.exceptions import ValidationError


class Moneda(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.nombre


# Join many to many entre Moneda y User
class MonedaUsuario(models.Model):
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cantidad = models.FloatField()

    def sumar_balance(self, cantidad):
        self.cantidad += cantidad
        self.save()

    def restar_balance(self, cantidad):
        if self.cantidad < cantidad:
            raise ValidationError("La cantidad a restar es menor al balance disponible")
        self.cantidad -= cantidad
        self.save()

    def __str__(self):
        return f'{self.moneda} - {self.usuario} - ${self.cantidad}'

    class Meta:
        unique_together = ('moneda', 'usuario')


class Transferencia(models.Model):
    usuario_origen = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_origen')
    usuario_destino = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_destino')
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    cantidad = models.FloatField()

    def __str__(self):
        return f'{self.usuario_origen} - {self.usuario_destino} - {self.moneda} - ${self.cantidad}'


# Signals
@receiver(post_save, sender=User)
def create_wallets(sender, instance, **kwargs):
    """
    Cada vez que se crea un usuario, inicializar wallets con balance 5 para cada moneda
    NOTA: balance 5 es solo para probar, en un ambiente real deberia ser 0
    """
    if not kwargs.get('created', False):
        return
    monedas = Moneda.objects.all()
    with transaction.atomic():
        for m in monedas:
            MonedaUsuario.objects.create(moneda=m, usuario=instance, cantidad=0)

@receiver(post_save, sender=Moneda)
def create_wallets(sender, instance, **kwargs):
    """
    Cada vez que se crea una moneda, inicializar wallets con balance 5 para cada usuario
    NOTA: balance 5 a modo de ejemplo, en un ambiente real debería ser 0
    """
    if not kwargs.get('created', False):
        return
    users = User.objects.all()
    with transaction.atomic():
        for u in users:
            MonedaUsuario.objects.create(moneda=instance, usuario=u, cantidad=0)
