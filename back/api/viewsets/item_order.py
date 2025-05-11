from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ModelViewSet

from api.models import ItemOrder
from api.serializers.item_order import ItemOrderSerializer

@extend_schema(tags=['ItemOrder'])
class ItemOrderViewSet(ModelViewSet):
    serializer_class = ItemOrderSerializer
    queryset = ItemOrder.objects.all()