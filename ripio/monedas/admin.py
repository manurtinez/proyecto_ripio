from django.contrib import admin

from monedas.models import Moneda, MonedaUsuario

# Register your models here.
admin.site.register(Moneda)
admin.site.register(MonedaUsuario)