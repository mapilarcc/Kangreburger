from rest_framework import status,views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from autApp.serializers.productosSerializer import ProductosSerializer

class ProductosCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer= ProductosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData={"Productos":request.data["Pedidos"],} #Preguntar
        tokenSerializer=TokenObtainPairSerializer(data=tokenData)   
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)

        
from django.conf import settings
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from autApp.models.Productos import Productos
from autApp.serializers.productosSerializer import Productos, ProductosSerializer

class ProductosDetailView(generics.RetrieveAPIView):
    queryset = Productos.objects.all()  
    serializer_class = ProductosSerializer
    permission_classes = (IsAuthenticated)

    def get_object(self, request, *args, **kwargs):
        token=request.META.get('HTTP_AUTHORIZATION')
        tokenbackend=TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data=tokenbackend.decode(token,verify=False)

        if valid_data['idCodigoDeProducto'] != kwargs['pk']:
            stringResponse={'detail':'Unathorizer Request'}
            return Response(stringResponse,status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)