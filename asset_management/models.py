from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100)
    # Add other fields as needed
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='asset_management_users',  # Add a unique related_name
        related_query_name='user',
    )

    # Add the related_name argument to the user_permissions field
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name='asset_management_users',  # Add a unique related_name
        related_query_name='user',
    )
    username = models.CharField(('username'), max_length=150, default='admin1234')
    password = models.CharField(('password'), max_length=150, default='admin1234')

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