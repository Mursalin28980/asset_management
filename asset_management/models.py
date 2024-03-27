from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.db import models
# Create your models here.


class Asset(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    barcode = models.CharField(max_length=50, unique=True)
    assigned = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    checkout_date = models.DateField(null=True, blank=True)
    # Add other fields as needed

class AssetUtilization(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add other fields as needed