# Generated by Django 4.1 on 2024-06-26 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_escala_id_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realizado',
            name='r_hora_ida',
        ),
        migrations.RemoveField(
            model_name='realizado',
            name='r_hora_volta',
        ),
        migrations.RemoveField(
            model_name='realizado',
            name='r_retorno',
        ),
        migrations.RemoveField(
            model_name='realizado',
            name='r_saida',
        ),
    ]