from rest_framework import status,views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from autApp.serializers.empleadosSerializer import EmpleadosSerializer

class UserCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer= EmpleadosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData={"username":request.data["Username"],
                   "password":request.data["Password"],} 
        tokenSerializer=TokenObtainPairSerializer(data=tokenData)   
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)


