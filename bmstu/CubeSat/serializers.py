from rest_framework import serializers
from .models import Products, Orders, OrdersToProducts


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"


class OrdersToProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdersToProducts
        fields = "__all__"
