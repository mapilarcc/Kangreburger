from django.conf import settings
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from autApp.models.Empleados import Empleados
from autApp.serializers.empleadosSerializer import Empleados, EmpleadosSerializer

class UserDetailView(generics.RetrieveAPIView):
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


