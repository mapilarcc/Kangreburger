from django.db import models
from .Clientes import Clientes
from .Empleados import Empleados
from .Pedidos import Pedidos


class CarritoDeCompras(models.Model):
  idCodigoDeVenta=models.BigAutoField(primary_key=True)
  cantidadProductos=models.CharField('cantidadProducto',max_length=80)
  ValorUnitario=models.IntegerField('valorUnitario',max_length=100)
  ValorTotal=models.IntegerField('valorTotal', max_length=100) 
  medioDePago=models.IntegerField('medioDePago', max_length=100)
  #EditarCarrito=
  idPedido=models.ForeignKey(Pedidos,related_name='Pedidos',on_delete=models.CASCADE)
  idClient=models.ForeignKey(Clientes,related_name='Clientes',on_delete=models.CASCADE)    
  idEmpleado=models.ForeignKey(Empleados,related_name='Empleados',on_delete=models.CASCADE)   