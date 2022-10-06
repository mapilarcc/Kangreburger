from django.db import models
from .Pedidos import Pedidos
from .Clientes import Clientes
from .Empleados import Empleados

class Facturacion(models.Model):
 idfactura=models.AutoField(primary_key=True)
 celCliente=models.IntegerField('Número de celular del cliente', max_length=50)
 medioPago=models.CharField('Medio de pago', max_length=80)
 valorTotal=models.IntegerField('Valor total', max_length=50)
 pedidos=models.ForeignKey(Pedidos,related_name='Facturacion',on_delete=models.CASCADE)
 clientes=models.ForeignKey(Clientes,related_name='Facturacion',on_delete=models.CASCADE)
 empleados=models.ForeignKey(Empleados,related_name='Facturacion',on_delete=models.CASCADE)