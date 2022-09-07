from dataclasses import field
import django_filters
from .models import Inventory

class InventoryFilter(django_filters.FilterSet):
    class Meta:
        model = Inventory
        fields = {'Kime_Verilecek': ['icontains'], 'Ürün_Ad': ['icontains'],
                  
        }