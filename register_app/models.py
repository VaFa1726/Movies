from django.db import models
from django.contrib.auth.models import User

# class UserProfile(models.Model):
class User(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=8)
    def __str__(self):
        return self.username