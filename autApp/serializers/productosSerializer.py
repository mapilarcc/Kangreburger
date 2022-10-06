from rest_framework import serializers
from autApp.models.Productos import Productos

class ProductosSerializer(serializers.ModelSerializer):
  class Meta:
   model = Productos
   fields = ['NomProducto', 'DescProducto','ValorUnitario']
  
