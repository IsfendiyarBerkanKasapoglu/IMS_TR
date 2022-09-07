from django.db import models

class Inventory(models.Model):
    Kime_Verilecek = models.CharField(max_length=100, null=True, blank=False)
    Ürün_Numarasi = models.CharField(max_length=100, unique=True, null=True, blank=False)
    Ürün_Ad = models.CharField(max_length=100, null=True, blank=False)
    Ürün_Cinsi = models.CharField(max_length=90, null=True, blank=False)
    Fiyati = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=False)
    Stok_Durumu = models.IntegerField(null=True, blank=False)
    Stok_Tarihi = models.DateField(null=True)
    


    def __str__(self) -> str:
        return self.Kime_Verilecek