from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiExample, OpenApiParameter
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.models import Brand
from api.serializers.brand import BrandSerializer


@extend_schema(tags=['Brand'], examples=[OpenApiExample('Бренд', value={'id': 1, 'name': 'Nike'})])
@extend_schema_view(
    list=extend_schema(
        summary="Получить все бренды",
    ),
    retrieve=extend_schema(
        summary="Получить конкретный бренд по его id",
    ),
)
class BrandViewSet(ReadOnlyModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
