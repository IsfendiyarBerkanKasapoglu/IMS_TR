from .widget import DatePickerInput, TimePickerInput, DateTimePickerInput
from django import forms 
from django.forms import ModelForm 
from .models import Inventory

class DateInput(forms.DateInput):
    input_type = 'date'

class AddInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ["Kime_Verilecek", "Ürün_Numarasi", "Ürün_Ad", "Ürün_Cinsi", "Fiyati", "Stok_Durumu", "Stok_Tarihi"]

        widgets = {
            'Stok_Tarihi': DateInput()
        }



class UpdateInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ["Kime_Verilecek", "Ürün_Ad", "Ürün_Cinsi", "Fiyati", "Stok_Durumu", "Stok_Tarihi"]

        widgets = {
            'Stok_Tarihi': DateInput()
        }