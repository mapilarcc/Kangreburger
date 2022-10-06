from rest_framework import serializers
from autApp.models.Facturacion import Facturacion

class FacturacionSerializer(serializers.ModelSerializer):
 class Meta:
  model = Facturacion
  fields = ['celCliente', 'medioPago', 'valorTotal', 'pedidos','clientes','empleados']

