# Generated by Django 4.1 on 2022-09-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_inventory_stok_tarihi'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='Kime_Verilecek',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
