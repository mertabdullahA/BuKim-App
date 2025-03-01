import random
import string
from django.db import models

def generate_random_code():
    length = 12  
    characters = string.ascii_letters + string.digits + string.punctuation 
    return ''.join(random.choices(characters, k=length))

class Users(models.Model):
    user_name = models.CharField(max_length=255)
    user_email = models.EmailField(max_length=255)
    user_password = models.CharField(max_length=255)
    user_registration_date = models.DateTimeField(auto_now_add=True)
    user_code = models.CharField(max_length=20, default=generate_random_code, unique=True) 

    def __str__(self):
        return self.user_name
