from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Address
from django.contrib.auth.decorators import login_required

@login_required
def add_address(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('lastName')
        phone_number = request.POST.get('phoneNumber')
        description = request.POST.get('description')
        user = request.user

        Address.objects.create(
            name=name,
            last_name=last_name,
            phone_number=phone_number,
            description=description,
            user=user
        )
        return JsonResponse({"success": True})
    return JsonResponse({"error": "Invalid method"}, status=405)

@login_required
def get_addresses(request):
    addresses = Address.objects.filter(user=request.user)
    return JsonResponse(list(addresses.values()), safe=False)

@login_required
def update_address(request, id):
    address = get_object_or_404(Address, id=id, user=request.user)
    if request.method == 'POST':
        address.name = request.POST.get('name', address.name)
        address.last_name = request.POST.get('lastName', address.last_name)
        address.phone_number = request.POST.get('phoneNumber', address.phone_number)
        address.description = request.POST.get('description', address.description)
        address.save()
        return JsonResponse({"success": True})
    return JsonResponse({"error": "Invalid method"}, status=405)

@login_required
def delete_address(request, id):
    address = get_object_or_404(Address, id=id, user=request.user)
    if request.method == 'DELETE':
        address.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"error": "Invalid method"}, status=405)
