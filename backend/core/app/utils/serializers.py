from rest_framework import serializers


class UnimplementedSerializer(serializers.Serializer):
    """
    Base class for API requests
    """

    def create(self, validated_data: dict) -> None:
        pass

    def update(self, instance: object, validated_data: dict) -> None:
        pass
