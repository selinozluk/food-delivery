from django.test import TestCase
from .models import Order

class OrderModelTest(TestCase):
    def test_string_representation(self):
        order = Order(total_price=100)
        self.assertEqual(str(order), f"Order {order.id}")
