from django.urls import path
from .views import get_past_orders, get_order_detail_by_id, complete_order, reorder

urlpatterns = [
    path('orders/', get_past_orders, name='get_past_orders'),
    path('orders/<int:id>/', get_order_detail_by_id, name='get_order_detail_by_id'),
    path('orders/complete/', complete_order, name='complete_order'),
    path('orders/reorder/<int:id>/', reorder, name='reorder'),
]
