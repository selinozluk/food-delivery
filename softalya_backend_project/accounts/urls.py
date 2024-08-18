from django.urls import path
from .views import add_address, get_addresses, update_address, delete_address
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('addresses/', login_required(get_addresses), name='get_addresses'),
    path('addresses/add/', login_required(add_address), name='add_address'),
    path('addresses/update/<int:id>/', login_required(update_address), name='update_address'),
    path('addresses/delete/<int:id>/', login_required(delete_address), name='delete_address'),
]
