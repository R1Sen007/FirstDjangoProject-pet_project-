from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from django.urls import reverse
from PIL import Image


class Adress(models.Model):
    city = models.CharField(max_length = 20)
    street = models.CharField(max_length = 20)
    house = models.IntegerField()

    def __str__(self):
        return ",".join([self.city[:3], self.street, str(self.house)])
    
    def get_absolute_url(self):
        return reverse('shop-create')


class Shop(models.Model):
    name = models.CharField(max_length = 20)
    adress = models.OneToOneField(Adress, on_delete= models.CASCADE, primary_key= True)
    image = models.ImageField(default="defaultShop.jpg", upload_to="shop_pic")
    description = models.CharField(max_length= 230, default="description should be here")
    ownerProfile = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return " ".join([self.name, str(self.adress)])
    
    def get_absolute_url(self):
        return reverse('shop-detail', kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs):
        super(Shop, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            size = (300, 300)
            img = self.expand2square(img, (0, 0, 0))
            img.thumbnail(size)
            img.save(self.image.path)

    def is_owner(self, user):
        return self.ownerProfile == user


    @staticmethod
    def expand2square(pil_img, background_color):
        width, height = pil_img.size
        if width == height:
            return pil_img
        elif width > height:
            result = Image.new(pil_img.mode, (width, width), background_color)
            result.paste(pil_img, (0, (width - height) // 2))
            return result
        else:
            result = Image.new(pil_img.mode, (height, height), background_color)
            result.paste(pil_img, ((height - width) // 2, 0))
            return result
        
    
class Products(models.Model):
    name = models.CharField(max_length= 20)
    price = models.IntegerField()
    amount = models.IntegerField()
    image = models.ImageField(default="defaultProduct.png", upload_to="product_pic")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Products, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            size = (300, 300)
            img.thumbnail(size)
            img.save(self.image.path)

    def is_owner(self, user):
        return self.shop.is_owner(user)            

    def get_absolute_url(self):
        return reverse('shop-detail', kwargs={'pk': self.shop.pk})

    def __str__(self):
        return  str(self.name)