from django.contrib import admin
from .models import Person, Adress, Owners, Products, Shop, ShopProducts
# Register your models here.
admin.site.register(Adress)
admin.site.register(Owners)
admin.site.register(Products)
admin.site.register(Shop)
admin.site.register(ShopProducts)

