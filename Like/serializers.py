from rest_framework import serializers
from Like.models import Like
from Logro.models import Logro
from Logro.serializers import LogroSerializer

class LikeSerializer(serializers.ModelSerializer):
    """Serializer para el modelo Like."""

    class Meta:
        model = Like
        fields = ['usuario', 'logro', 'fecha_like']

class LikeLogroSerializer(serializers.ModelSerializer):
    """Serializer para mostrar la información de un like junto con el logro asociado."""

    logro = LogroSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['usuario', 'logro', 'fecha_like']
        read_only_fields = ['usuario', 'logro']  # Los campos 'usuario' y 'logro' no se pueden modificar desde el cliente

class ConteoLikesSerializer(serializers.Serializer):
    """Serializer para mostrar el conteo de likes de un logro."""

    cantidad_likes = serializers.IntegerField(read_only=True)

    def update(self, instance, validated_data):
        """No se permite actualizar el conteo de likes."""
        pass

    def create(self, validated_data):
        """No se permite crear el conteo de likes."""
        pass