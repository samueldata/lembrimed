# Generated by Django 4.2.11 on 2024-04-21 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Medicamento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("codigo", models.CharField(max_length=20, unique=True)),
                ("nome", models.CharField(max_length=100)),
                ("apresentacao", models.CharField(max_length=100)),
            ],
        ),
    ]
