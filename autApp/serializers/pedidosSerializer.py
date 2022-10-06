from rest_framework import serializers
from autApp.models.Pedidos import Pedidos

class PedidosSerializer(serializers.ModelSerializer):
 class Meta:
  model = Pedidos
  fields = ['Codproduct']
