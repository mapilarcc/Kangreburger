from rest_framework import serializers
from autApp.models.CarritoDeCompras import CarritoDeCompras


class CarritoDeComprasSerializer(serializers.ModelSerializer):
 class Meta:
  model = CarritoDeCompras
  fields = ['cantidadProductos', 'ValorUnitario','ValorTotal','medioDePago']
