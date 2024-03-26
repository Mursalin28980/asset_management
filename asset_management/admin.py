from django.contrib import admin
from .models import User, Asset, AssetUtilization
# Register your models here.
admin.site.register(User)
admin.site.register(Asset)
admin.site.register(AssetUtilization)