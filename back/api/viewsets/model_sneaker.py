from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.models import ModelSneaker
from api.serializers.model_sneaker import ModelSneakerSerializer

@extend_schema(tags=['ModelSneaker'])
@extend_schema_view(
    list=extend_schema(
        summary="Получить все модели кроссовок",
    ),
    retrieve=extend_schema(
        summary="Получить конкретную модель по ее id",
    ),
)
class ModelSneakerViewSet(ReadOnlyModelViewSet):
    serializer_class = ModelSneakerSerializer
    queryset = ModelSneaker.objects.all()
