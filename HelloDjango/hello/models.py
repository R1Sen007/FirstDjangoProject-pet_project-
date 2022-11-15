from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 20)
    age = models.IntegerField()

class Adress(models.Model):
    city = models.CharField(max_length = 20)
    street = models.CharField(max_length = 20)
    house = models.IntegerField()
    
class Owners(models.Model):
    name = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 20)

class Products(models.Model):
    name = models.CharField(max_length= 20)
    created = models.DateField()

class Shop(models.Model):
    name = models.CharField(max_length = 20)
    product = models.ManyToManyField(Products, through="ShopProducts")
    adress = models.OneToOneField(Adress, on_delete= models.CASCADE, primary_key= True)
    owner = models.ForeignKey(Owners, on_delete= models.CASCADE)

class ShopProducts(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    count = models.IntegerField()
    value = models.IntegerField()


