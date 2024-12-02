
import os
from django.db import models
from django.contrib.auth.models import AbstractUser	# AbstractUser 불러오기



class User(AbstractUser):
    profile_name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to="image/profile_image", blank=True )

  
            
            