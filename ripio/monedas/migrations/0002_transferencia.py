# Generated by Django 4.1.1 on 2022-09-15 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("monedas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transferencia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("cantidad", models.FloatField()),
                (
                    "moneda",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="monedas.moneda"),
                ),
                (
                    "usuario_destino",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="usuario_destino",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "usuario_origen",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="usuario_origen",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
