from django.http import Http404
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.models import User
from api.serializers.user import UserSerializer

@extend_schema(tags=['User'])
class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=['get'], url_path='by_tg_id/(?P<user_tg_id>[^/.]+)')
    def get_items_by_user(self, request, user_tg_id=None):
        try:
            user = self.queryset.get(tg_id=user_tg_id)
        except User.DoesNotExist:
            raise Http404("No user data found for the given tg ID.")
        serializer = self.get_serializer(user)
        return Response(serializer.data)