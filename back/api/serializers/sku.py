from rest_framework import serializers
from django.conf import settings
from urllib.parse import urljoin

from api.models import SKU


class SKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = '__all__'

class SKUByModelSneakerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='model_sneaker.name')
    brand = serializers.CharField(source='model_sneaker.brand.name')
    color = serializers.CharField(source='model_sneaker.color')
    image_url = serializers.ImageField(source='model_sneaker.image_url')
    size = serializers.CharField(source='size.__str__')
    class Meta:
        model = SKU
        fields = ['id', 'name', 'brand', 'image_url', 'color', 'size', 'price', 'count']