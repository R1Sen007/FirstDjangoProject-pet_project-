from django.contrib import admin
from .models import Adress, Products, Shop


class AdressAdmin(admin.ModelAdmin):
    list_display = ("id", "city", "street", "house",)

    
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


class ShopAdmin(admin.ModelAdmin):
    list_display = ("name", "adress", "ownerProfile",) # , "product"


admin.site.register(Adress, AdressAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Shop, ShopAdmin)


