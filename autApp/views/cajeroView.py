from rest_framework import status,views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from autApp.serializers.empleadosSerializer import EmpleadosSerializer

class CajeroCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer= EmpleadosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData={"username":request.data["Username"],
                   "password":request.data["Password"]} 
        tokenSerializer=TokenObtainPairSerializer(data=tokenData)   
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)


from django.conf import settings
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from autApp.models.Empleados import Empleados
from autApp.serializers.empleadosSerializer import Empleados, EmpleadosSerializer

class CajeroDetailView(generics.RetrieveAPIView):
    queryset = Empleados.objects.all()  
    serializer_class = EmpleadosSerializer
    permission_classes = (IsAuthenticated)

    def get_object(self, request, *args, **kwargs):
        token=request.META.get('HTTP_AUTHORIZATION')
        tokenbackend=TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data=tokenbackend.decode(token,verify=False)

        if valid_data['idEmpleados'] != kwargs['pk']:
            stringResponse={'detail':'Unathorizer Request'}
            return Response(stringResponse,status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)
