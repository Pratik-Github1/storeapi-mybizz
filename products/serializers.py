from rest_framework import serializers
from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    foreign_currency = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'price', 'foreign_currency',
            'description', 'category', 'image',
            'rating_rate', 'rating_count', 'created_at', 'updated_at'
        ]

    def get_price(self, obj):
        return f"${obj.price:.2f}"


    def get_foreign_currency(self, obj):
        inr = obj.price * 80
        return f"₹{inr:,.2f}"


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title', 'price', 'description', 'category', 'image',
            'rating_rate', 'rating_count'
        ]

class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title', 'price', 'description', 'category', 'image',
            'rating_rate', 'rating_count', 'created_at', 'updated_at'
        ]
        extra_kwargs = {
            'created_at': {'required': False},
            'updated_at': {'required': False}
        }
