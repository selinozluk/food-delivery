from django.urls import path
from .views import home, register, login, add_address, get_addresses, update_address, delete_address

urlpatterns = [
    path('users/', home, name='home'),  # Ana sayfa
    path('users/register/', register, name='register'),  # Kayıt sayfası
    path('users/login/', login, name='login'),  # Giriş sayfası
    path('users/addresses/', get_addresses, name='get_addresses'),  # Adresleri görüntüleme
    path('users/addresses/add/', add_address, name='add_address'),  # Adres ekleme
    path('users/addresses/update/<int:id>/', update_address, name='update_address'),  # Adres güncelleme
    path('users/addresses/delete/<int:id>/', delete_address, name='delete_address'),  # Adres silme
]
