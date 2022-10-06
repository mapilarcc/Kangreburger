from django.db import models

class Productos(models.Model):
  idCodigoDeProducto=models.BigAutoField(primary_key=True)
  NomProducto=models.CharField('nombreDeProducto',max_length=100)
  DescProducto=models.CharField('descripcionDeProducto',max_length=200)
  ValorUnitario=models.IntegerField('valorUnitario',max_length=100)

