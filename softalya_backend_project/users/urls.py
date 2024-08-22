from django.urls import path
from .views import home, register, login, add_address, get_addresses, update_address, delete_address

urlpatterns = [
    path('', home, name='home'),  # Ana sayfa
    path('register/', register, name='register'),  # Kayıt sayfası
    path('login/', login, name='login'),  # Giriş sayfası
    path('addresses/', get_addresses, name='get_addresses'),  # Adresleri görüntüleme
    path('addresses/add/', add_address, name='add_address'),  # Adres ekleme
    path('addresses/update/<int:id>/', update_address, name='update_address'),  # Adres güncelleme
    path('addresses/delete/<int:id>/', delete_address, name='delete_address'),  # Adres silme
]
