from rest_framework import serializers
from autApp.models.Clientes import Clientes

class ClientesSerializer(serializers.ModelSerializer):
 class Meta:
  model = Clientes
  fields = ['nameCliente', 'celCliente','account']
