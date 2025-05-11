from rest_framework import serializers

from api.models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'user', 'sku', 'quantity']


class CartItemGetSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='sku.model_sneaker.name')
    brand = serializers.CharField(source='sku.model_sneaker.brand.name')
    color = serializers.CharField(source='sku.model_sneaker.color')
    image_url = serializers.ImageField(source='sku.model_sneaker.image_url')
    size = serializers.CharField(source='sku.size.__str__')
    price = serializers.IntegerField(source='sku.price')
    class Meta:
        model = CartItem
        fields = ['id', 'user', 'sku', 'name', 'brand', 'image_url', 'color', 'size', 'price', 'quantity']


class CartItemUpdateSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField()
    class Meta:
        model = CartItem
        fields = ['quantity']

    def update(self, instance, validated_data):
        instance.quantity = validated_data['quantity']
        instance.save()
        return instance