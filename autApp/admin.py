from django.contrib import admin
from .models.Empleados import Empleados
from .models.Productos import Productos
from .models.Pedidos import Pedidos
from .models.Clientes import Clientes
from .models.CarritoDeCompras import CarritoDeCompras
from .models.Facturacion import Facturacion

# Register your models here.

admin.site.register(Empleados)
admin.site.register(Productos)
admin.site.register(Pedidos)
admin.site.register(Clientes)
admin.site.register(CarritoDeCompras)
admin.site.register(Facturacion)



# Register your models here.
