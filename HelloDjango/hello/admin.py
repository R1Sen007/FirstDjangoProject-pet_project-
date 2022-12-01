from django.contrib import admin
from .models import Adress, Owners, Products, Shop, ShopProducts
# Register your models here.

class AdressAdmin(admin.ModelAdmin):
    list_display = ("id", "city", "street", "house")

class OwnersAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "surname")
    
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created")

class ShopAdmin(admin.ModelAdmin):
    list_display = ("name", "adress", "owner") # , "product"


admin.site.register(Adress, AdressAdmin)
admin.site.register(Owners, OwnersAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(ShopProducts)

