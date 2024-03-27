from django.contrib import admin
from .models import  Asset, AssetUtilization
# Register your models here.

admin.site.register(Asset)
admin.site.register(AssetUtilization)