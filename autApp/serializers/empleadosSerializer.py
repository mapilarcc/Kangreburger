from rest_framework import serializers
from autApp.models.Empleados import Empleados


class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = ('NombreEmpleados', 'CelEmpleado', 'CCEmpleado','Rol','Status','username', 'password')
    