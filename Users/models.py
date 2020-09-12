from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(default='default.jpg', blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
