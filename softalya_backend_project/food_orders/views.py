from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def order_list(request):
    return HttpResponse("Order list")

def order_details(request, order_id):
    return HttpResponse(f"Order details for order id: {order_id}")
