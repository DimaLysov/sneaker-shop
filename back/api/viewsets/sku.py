from django.http import Http404
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from yaml import serialize

from api.models import SKU
from api.serializers.sku import SKUSerializer, SKUByModelSneakerSerializer


@extend_schema(tags=['SKU'])
@extend_schema_view(
    list=extend_schema(
        summary="Получить все записи из sku",
    ),
    retrieve=extend_schema(
        summary="Получить конкретную запись по ее id",
    ),
)
class SKUViewSet(ReadOnlyModelViewSet):
    serializer_class = SKUSerializer
    queryset = SKU.objects.all()

    @action(detail=False, methods=['get'], url_path='by-model_sneaker/(?P<model_sneaker_id>[^/.]+)',
            serializer_class=SKUByModelSneakerSerializer)
    def get_sku_by_model_sneaker(self, request, model_sneaker_id=None):
        sku = self.queryset.filter(model_sneaker=model_sneaker_id).order_by('size__size_rus')

        if not sku.exists():
            raise Http404("No SKU data found for the given model_sneaker ID.")

        serializer = self.serializer_class(sku, context={'request': request}, many=True)
        return Response(serializer.data)
