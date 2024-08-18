from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Order, OrderItem, Address
from django.contrib.auth.decorators import login_required

@login_required
def get_past_orders(request):
    # Kullanıcının geçmiş siparişlerini getirir
    orders = Order.objects.filter(user=request.user)
    return JsonResponse(list(orders.values()), safe=False)

@login_required
def get_order_detail_by_id(request, id):
    # Belirli bir siparişin detaylarını getirir
    order = get_object_or_404(Order, id=id, user=request.user)
    order_items = OrderItem.objects.filter(order=order)
    return JsonResponse({"order": order.id, "items": list(order_items.values())}, safe=False)

@login_required
def complete_order(request):
    if request.method == 'POST':
        # Kullanıcının sepetindeki ürünleri al
        cart_items = request.user.cart.cartitem_set.all()

        if not cart_items:
            return JsonResponse({"error": "Sepetinizde ürün bulunmamaktadır."}, status=400)

        # Yeni bir sipariş oluştur
        address_id = request.POST.get('addressId')
        address = get_object_or_404(Address, id=address_id, user=request.user)
        order = Order.objects.create(user=request.user, address=address, total_price=0)

        # Sepetteki ürünleri siparişe ekle ve toplam fiyatı güncelle
        for item in cart_items:
            order_item = OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )
            order.total_price += order_item.price * order_item.quantity

        # Toplam fiyatı kaydet
        order.save()

        # Sepeti temizle
        request.user.cart.cartitem_set.all().delete()

        return JsonResponse({"success": True, "order_id": order.id})
    return JsonResponse({"error": "Invalid method"}, status=405)

@login_required
def reorder(request, id):
    if request.method == 'POST':
        # Mevcut siparişi al
        original_order = get_object_or_404(Order, id=id, user=request.user)
        
        # Yeni bir sipariş oluştur
        new_order = Order.objects.create(
            user=request.user,
            address=original_order.address,
            total_price=0  # Başlangıçta 0, sonra hesaplanacak
        )

        # Eski siparişteki ürünleri yeni siparişe ekle
        original_order_items = original_order.orderitem_set.all()
        for item in original_order_items:
            new_order_item = OrderItem.objects.create(
                order=new_order,
                product=item.product,
                price=item.price,
                quantity=item.quantity
            )
            new_order.total_price += new_order_item.price * new_order_item.quantity

        # Yeni siparişin toplam fiyatını kaydet
        new_order.save()

        return JsonResponse({"success": True, "order_id": new_order.id})
    return JsonResponse({"error": "Invalid method"}, status=405)
