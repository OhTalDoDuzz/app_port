# Generated by Django 4.1 on 2024-06-27 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_escala_id_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='escala',
            name='valor_hotel',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='realizado',
            name='r_valor_hotel',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='realizado',
            name='valor_hotel',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
