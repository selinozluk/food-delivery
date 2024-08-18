from django.contrib import admin
from .models import Address  # Sadece Address modelini import ettim

admin.site.register(Address)
