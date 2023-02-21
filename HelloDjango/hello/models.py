from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from django.urls import reverse


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 20)
    age = models.IntegerField()


class Adress(models.Model):
    city = models.CharField(max_length = 20)
    street = models.CharField(max_length = 20)
    house = models.IntegerField()

    def __str__(self):
        return ",".join([self.city[:3], self.street, str(self.house)])
    
    def get_absolute_url(self):
        return reverse('shop-create')


# class Owners(models.Model):
#     name = models.CharField(max_length = 20)
#     surname = models.CharField(max_length = 20)

#     def __str__(self):
#         return  " ".join([self.name,self.surname])


class Products(models.Model):
    name = models.CharField(max_length= 20)
    created = models.DateField(default=None)
    def __str__(self):
        return  str(self.name)


class Shop(models.Model):
    name = models.CharField(max_length = 20)
    product = models.ManyToManyField(Products, through="ShopProducts")
    adress = models.OneToOneField(Adress, on_delete= models.CASCADE, primary_key= True)
    ownerProfile = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return " ".join([self.name, str(self.adress)])
    
    def get_absolute_url(self):
        return reverse('shop-detail', kwargs={'pk': self.pk})


class ShopProducts(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    count = models.IntegerField()
    value = models.IntegerField()

    def __str__(self):
        return " ".join([str(self.products), str(self.shop)])


