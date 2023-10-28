from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .models import IoTObject, IoTData
from rest_framework import generics
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework import viewsets

@api_view(['POST'])
def creer_objet_iot(request):
    # Récupérez les données d'objet IoT depuis la requête POST
    data = request.data

    # Créez un nouvel objet IoT
    iot_object = IoTObject.objects.create(
        name=data['name'],  # Exemple de champ pour le nom
        # Autres champs pour décrire l'objet IoT
    )

    # Générez un token pour l'objet IoT
    token, created = Token.objects.get_or_create(user=iot_object)

    return Response({'token': token.key}, status=status.HTTP_201_CREATED)


# --------------------


from iotapp.serializers import IoTObjectDetailSerializer, IoTObjectListSerializer,\
    IoTDataDetailSerializer, IoTDataListSerializer


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class AdminIoTObjectViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = IoTObjectListSerializer
    detail_serializer_class = IoTObjectDetailSerializer
    queryset = IoTObject.objects.all()

class AdminIoTDataViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = IoTDataListSerializer
    detail_serializer_class = IoTDataDetailSerializer
    queryset = IoTData.objects.all()


class IoTObjectViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = IoTObjectListSerializer
    detail_serializer_class = IoTObjectDetailSerializer

    def get_queryset(self):
        return IoTObject.objects.filter(active=True)

    @action(detail=True, methods=['post'])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()


class IoTDataViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = IoTDataListSerializer

    @action(detail=False, methods=['post'])
    def create_data_with_auth_token(self, request):
        auth_token = request.query_params.get('auth_token', None)
        if not auth_token:
            return Response({'error': 'auth_token parameter is required in the URL.'}, status=status.HTTP_BAD_REQUEST)

        # Search for the IoTObject with the given auth_token
        try:
            iot_object = IoTObject.objects.get(auth_token=auth_token)
        except IoTObject.DoesNotExist:
            return Response({'error': 'IoTObject not found with the provided auth_token.'}, status=status.HTTP_NOT_FOUND)

        # Create an IoTData associated with the IoTObject
        data = request.data
        data['object'] = iot_object.id  # Set the object to the IoTObject
        serializer = IoTDataListSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'IoTData created successfully.'}, status=status.HTTP_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_BAD_REQUEST)