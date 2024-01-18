from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PasswordVault(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website_name = models.CharField(max_length=250)
    website_link = models.URLField()
    website_password = models.CharField(max_length=100)
    date = models.DateTimeField()
    
    def __str__(self):
        return self.website_name