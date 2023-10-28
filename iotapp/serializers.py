from rest_framework import serializers
from iotapp.models import IoTObject, IoTData

class IoTDataListSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(write_only=True)

    class Meta:
        model = IoTData
        fields = ['id', 'timestamp', 'temperature', 'humidity', 'auth_token']

    def create(self, validated_data):
        auth_token = validated_data.pop('auth_token', None)
        if auth_token:
            try:
                iot_object = IoTObject.objects.get(auth_token=auth_token)
                validated_data['object'] = iot_object
            except IoTObject.DoesNotExist:
                raise serializers.ValidationError('IoTObject not found with the provided auth_token.')

        iot_data = IoTData.objects.create(**validated_data)
        return iot_data

class IoTDataDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = IoTData
        fields = ['id', 'timestamp', 'temperature', 'humidity', 'object']

    # def get_articles(self, instance):
    #     queryset = instance.articles.filter(active=True)
    #     serializer = ArticleSerializer(queryset, many=True)
    #     return serializer.data


class IoTObjectListSerializer(serializers.ModelSerializer):

    class Meta:
        model = IoTObject
        fields = ['id', 'name', 'auth_token']

    # def validate_name(self, value):
    #     if IoTObject.objects.filter(name=value).exists():
    #         raise serializers.ValidationError('IoTObject already exists')
    #     return value

    # def validate(self, data):
    #     if data['name'] not in data['description']:
    #         raise serializers.ValidationError('Name must be in description')
    #     return data


class IoTObjectDetailSerializer(serializers.ModelSerializer):

    datas = serializers.SerializerMethodField()

    class Meta:
        model = IoTObject
        fields = ['id', 'name', 'auth_token', 'datas']

    def get_datas(self, instance):
        queryset = instance.datas
        serializer = IoTDataListSerializer(queryset, many=True)
        return serializer.data