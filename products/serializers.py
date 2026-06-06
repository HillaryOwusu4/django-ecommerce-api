from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product        # which model to serialize
        fields = '__all__'     # include all columns