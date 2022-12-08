from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')
    
    
    def __str__(self):
        return " ".join([self.user.first_name, self.user.last_name])

    def get_mini_profile_pic(self):
        img = Image.open(self.image.path)
        img.thumbnail((300,300))
        
    

# Create your models here.
