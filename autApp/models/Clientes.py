from django.db import models

class Clientes(models.Model):
 idCliente=models.BigAutoField(primary_key=True)
 nameCliente=models.CharField('Nombre del cliente: ', max_length=80)
 celCliente=models.IntegerField('Número de celular del cliente: ', max_length=30)