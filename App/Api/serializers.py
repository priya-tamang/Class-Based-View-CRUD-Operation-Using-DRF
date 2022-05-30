from rest_framework import serializers
from App.models import App


class detailSerializers(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
    num = serializers.CharField()


    def create(self, validated_data):
        return App.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address',instance.address)
        instance.num = validated_data.get('num',instance.num)
        instance.save()
        return instance