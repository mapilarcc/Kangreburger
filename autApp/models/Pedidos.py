from django.db import models
from .Productos import Productos

class Pedidos(models.Model):
 idpedido=models.AutoField(primary_key=True)
 Codproduct=models.ForeignKey(Productos,related_name='Pedidos',on_delete=models.CASCADE)