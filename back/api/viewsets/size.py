from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.models import Size
from api.serializers.size import SizeSerializer

@extend_schema(tags=['Size'])
@extend_schema_view(
    list=extend_schema(
        summary="Получить все размеры",
    ),
    retrieve=extend_schema(
        summary="Получить конкретный размер по его id",
    ),
)
class SizeViewSet(ReadOnlyModelViewSet):
    serializer_class = SizeSerializer
    queryset = Size.objects.all()
