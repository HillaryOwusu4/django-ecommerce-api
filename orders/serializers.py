from rest_framework import serializers
from products.models import Product
from products.serializers import ProductSerializer 
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # Nested serializer for product details
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)  # For creating/updating orders
    class Meta:
        model = Order
        fields = '__all__'