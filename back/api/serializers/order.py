from rest_framework import serializers

from api.models import Order, User
from api.serializers.item_order import ItemOrderAllDataSerializer


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderGetNewOrderSerializer(serializers.ModelSerializer):
    user_tg_id = serializers.CharField(source='user.tg_id')
    items = ItemOrderAllDataSerializer(many=True, source='itemorder_set')

    class Meta:
        model = Order
        fields = ['user_tg_id', 'fullname', 'phone_number', 'delivery_address', 'items']


class OrderCreateSerializer(serializers.Serializer):
    tg_id = serializers.IntegerField(write_only=True)
    fullname = serializers.CharField(max_length=300)
    phone_number = serializers.IntegerField()
    delivery_address = serializers.CharField(max_length=300)
    # class Meta:
    #     model = Order
    #     fields = ['tg_id', 'fullname', 'phone_number', 'delivery_address']

    def create(self, validated_data):
        user = User.objects.get(tg_id=validated_data['tg_id'])
        order = Order.objects.create(
            user=user,
            fullname=validated_data['fullname'],
            phone_number=validated_data['phone_number'],
            delivery_address=validated_data['delivery_address'],
        )
        return order
