from rest_framework import serializers
from main.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'rank', 'product_dimensions', 'price',
                  'sale_price', 'url', 'asin', 'image')
