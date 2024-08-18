from django.contrib import admin
from django.urls import path
from .views import home  # Yeni oluşturduğunuz view'ı buraya import edin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Ana sayfa URL yönlendirmesi
]
