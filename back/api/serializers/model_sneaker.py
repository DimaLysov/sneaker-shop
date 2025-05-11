from rest_framework import serializers

from api.models import ModelSneaker


class ModelSneakerSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source='brand.name')
    class Meta:
        model = ModelSneaker
        fields = ['id', 'name', 'brand', 'color', 'image_url']
