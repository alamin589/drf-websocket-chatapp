from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)