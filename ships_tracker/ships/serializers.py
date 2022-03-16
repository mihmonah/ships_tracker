from rest_framework import serializers


class ShipOwnerSerializer(serializers.Serializer):
    username = serializers.CharField(help_text="Username владельца судна")


class ShipSerializer(serializers.Serializer):
    created_at = serializers.DateTimeField(allow_null=True, help_text="Дата и время создания")
    code = serializers.CharField(allow_null=True, help_text="Уникальный код судна")
    name = serializers.CharField(allow_null=True, help_text="Имя судна")
    owner = ShipOwnerSerializer(allow_null=True)


class ShipMovementHistorySerializer(serializers.Serializer):
    created_at = serializers.DateTimeField(allow_null=True, help_text="Дата и время создания")
    geo_datetime = serializers.DateTimeField(allow_null=True, help_text="Дата и время определения геопозиции судна")
    longitude = serializers.CharField(allow_null=True, help_text="Долгота")
    width = serializers.CharField(allow_null=True, help_text="Широта")
    owner = ShipOwnerSerializer(allow_null=True)
