# Generated by Django 2.2.20 on 2021-06-04 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturaxion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='metodoPago',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='factura',
            name='tipoComprobante',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='factura',
            name='total',
            field=models.CharField(default='', max_length=10),
        ),
    ]
