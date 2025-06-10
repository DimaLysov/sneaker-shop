from django.db import transaction
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import Order, CartItem, ItemOrder, SKU
from api.serializers.order import OrderSerializer, OrderGetNewOrderSerializer, OrderCreateSerializer


@extend_schema(tags=['Order'])
@extend_schema_view(
    list=extend_schema(
        summary="Получить все заказы",
    ),
)
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return OrderCreateSerializer
        return OrderSerializer

    @action(detail=False, methods=['get'], url_path='new-order', serializer_class=OrderGetNewOrderSerializer)
    def get_new_order(self, request):
        new_orders = self.queryset.filter(status='new')
        serializer = self.serializer_class(new_orders, many=True)
        answer = serializer.data
        self.queryset.update(status='processing')
        return Response(answer)

    # @action(detail=True, methods=['post'], serializer_class=OrderCreateSerializer)
    @transaction.atomic()
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order = serializer.save()
        cart_items = CartItem.objects.filter(user=order.user)
        for item in cart_items:
            sku = SKU.objects.get(pk=item.sku.pk)
            item_order = ItemOrder.objects.create(
                order=order,
                sku=sku,
                quantity=item.quantity,
                price=sku.price
            )
            sku.count -= item.quantity
            sku.save()
        cart_items.delete()
        return Response(serializer.data)
