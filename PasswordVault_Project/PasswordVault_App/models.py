from django.db import models


# Create your models here.
class PasswordVault(models.Model):
    website_name = models.CharField(max_length=250)
    website_link = models.URLField()
    website_password = models.CharField(max_length=100)
    date = models.DateTimeField()
    
    def __str__(self):
        return self.website_name  