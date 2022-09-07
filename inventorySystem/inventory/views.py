from django.shortcuts import get_object_or_404, render, redirect
from .models import Inventory
from django.contrib.auth.decorators import login_required
from .forms import AddInventoryForm, UpdateInventoryForm
from django.contrib import messages
from .filters import InventoryFilter

@login_required
def inventory_list(request):
    inventories = Inventory.objects.all()
    inventories_filter = InventoryFilter(request.GET, queryset=inventories)
    context = {
        "inventories_filter": inventories_filter,
        "title": "Inventory List",
        "inventories": inventories,
        

    }
    return render(request, "inventory/inventory_list.html", context=context)


@login_required
def per_product_view(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    context = {
        'inventory': inventory
    }

    return render(request, "inventory/per_product.html", context=context)

@login_required
def add_product(request):
    add_form = AddInventoryForm()
    if request.method == "POST":
        add_form = AddInventoryForm(data=request.POST)
        if add_form.is_valid():
            add_form.save()
            messages.success(request, "Ürün Eklendi")
            return redirect("/inventory")
  
    return render(request, "inventory/inventory_add.html", {"form": add_form})

@login_required
def delete_inventory(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    inventory.delete()
    messages.warning(request, "Ürün Silindi")
    return redirect("/inventory")


@login_required
def update_inventory(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        updateForm = UpdateInventoryForm(data=request.POST)
        if updateForm.is_valid():
            inventory.Kime_Verilecek = updateForm.data['Kime_Verilecek']
            inventory.Ürün_Ad = updateForm.data['Ürün_Ad']
            inventory.Ürün_Cinsi = updateForm.data['Ürün_Cinsi']
            inventory.Fiyati = updateForm.data['Fiyati']
            inventory.Stok_Durumu = updateForm.data['Stok_Durumu']
            inventory.Stok_Tarihi = updateForm.data['Stok_Tarihi']
            messages.info(request, "Ürün Güncellendi")
            inventory.save()

            return redirect(f"/inventory/per_product/{pk}")
            
    else:
        updateForm = UpdateInventoryForm(instance=inventory)

    context = {"form": updateForm}
    return render(request, "inventory/inventory_update.html", context=context)
