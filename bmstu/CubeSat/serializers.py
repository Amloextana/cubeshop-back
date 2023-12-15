from rest_framework import serializers
from .models import Products, Orders, OrdersToProducts, Categories


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "category_name"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"


class OrdersToProductsSerializer(serializers.ModelSerializer):
    product = ProductsSerializer(source="product_ref")

    class Meta:
        model = OrdersToProducts
        fields = ('amount', 'product')


class OrderWithProductsSerializer(serializers.ModelSerializer):
    orders_products = OrdersToProductsSerializer(many=True, source="orderstoproducts_set")
    class Meta:
        model = Orders
        fields = ('status', 'created_at', 'formed_at', 'completed_at', 'moderator', 'customer', 'orders_products')



