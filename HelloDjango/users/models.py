from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # img = ???

    def __str__(self):
        return " ".join([self.user.first_name, self.user.last_name])

    

# Create your models here.
