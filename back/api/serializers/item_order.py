from rest_framework import serializers

from api.models import ItemOrder


class ItemOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOrder
        fields = '__all__'


class ItemOrderAllDataSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='sku.model_sneaker.name')
    brand = serializers.CharField(source='sku.model_sneaker.brand.name')
    color = serializers.CharField(source='sku.model_sneaker.color')
    size = serializers.CharField(source='sku.size.__str__')

    class Meta:
        model = ItemOrder
        fields = ['name', 'brand', 'color', 'size', 'price', 'quantity']