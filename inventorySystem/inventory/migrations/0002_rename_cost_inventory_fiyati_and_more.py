# Generated by Django 4.1 on 2022-09-02 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='Cost',
            new_name='Fiyati',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='Stock',
            new_name='Stok_Durumu',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='Stock_Date',
            new_name='Stok_Tarihi',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='Product_Name',
            new_name='Ürün_Ad',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='Product_Type',
            new_name='Ürün_Cinsi',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='Unique_Number',
            new_name='Ürün_Numarasi',
        ),
    ]
