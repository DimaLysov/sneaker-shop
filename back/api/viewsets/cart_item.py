from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.models import CartItem
from api.serializers.cart_item import CartItemSerializer, CartItemUpdateSerializer, CartItemGetSerializer


@extend_schema(tags=['CartItem'])
@extend_schema_view(
    list=extend_schema(
        summary='Получить все данные из таблицы',
    ),
    retrieve=extend_schema(
        summary='Получить конкретную запись по ее id',
    ),
    create=extend_schema(
        summary='Добавить запись в таблицу',
        description='Для добавления необходимо: id пользователя, id sku, количество выбранного товара в корзине',
    ),
    destroy=extend_schema(
        summary='Удалить запись из таблицы',
        description='Для удаления необходимо указать id записи'
    )
)
class CartItemViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    @extend_schema(summary='Получить все товары пользователя по ID',
                   description='Необходимо указать id пользователя')
    @action(detail=False, methods=['get'], url_path='by-user/(?P<user_id>[^/.]+)', serializer_class=CartItemGetSerializer)
    def get_items_by_user(self, request, user_id=None):
        cart_items = self.queryset.filter(user=user_id)
        serializer = self.get_serializer(cart_items, many=True)
        return Response(serializer.data)

    @extend_schema(summary='Обновить количество для конкретного товара в корзине',
                   description='Необходимо указать id записи, а также передать новое значение поля "quantity"')
    @action(detail=True, methods=['patch'], url_path='update-quantity', serializer_class=CartItemUpdateSerializer)
    def update_quantity(self, request, pk=None):
        cart_item = self.get_object()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.update(cart_item, serializer.validated_data)

        return Response(self.get_serializer(cart_item).data)

    