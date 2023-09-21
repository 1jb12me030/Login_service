from django.db import models

# Create your models here.
# login_service/models.py
from django.db import models
from django.contrib.auth.models import User as AuthUser

class Referral(models.Model):
    code = models.CharField(max_length=10, unique=True)
    

class UserProfile(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    referral_code = models.CharField(max_length=10, unique=True)
    
