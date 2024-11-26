
import os
from django.db import models
from django.contrib.auth.models import AbstractUser	# AbstractUser 불러오기



class User(AbstractUser):
    profile_name = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to="image/profile_image", blank=True )

    def __del__(self):
        
        user_dir_path = "./media/userfiles/"+self.username+"/"
        
        print(user_dir_path)
        
        if os.path.exists(user_dir_path):
            print('exist')
            os.remove(user_dir_path)
            os.rmdir(user_dir_path)
        else :
            print('없음')
            
            