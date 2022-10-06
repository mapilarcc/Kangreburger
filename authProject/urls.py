from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
from autApp.views import userCreateView,userDetailView,superadminView,productosView,meseroView,facturacionView,clienteView,cajeroView

urlpatterns = [ 
    path('login/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('user/',userCreateView.UserCreateView.as_view()),
    path('user/<int:pk>/',userDetailView.UserDetailView.as_view()),
    path('productos/',productosView.ProductosCreateView.as_view()),
    path('productos/<int:pk>/',productosView.ProductosDetailView.as_view()),
    path('facturacion/',facturacionView.FacturacionCreateView.as_view()),
    path('facturacion/<int:pk>/',facturacionView.FacturacionDetailView.as_view()),
    path('superadmin/',superadminView.SuperadminCreateView.as_view()),
    path('superadmin/<int:pk>/',superadminView.SuperadminDetailView.as_view()),
    path('mesero/',meseroView.MeseroCreateView.as_view()),
    path('mesero/<int:pk>/',meseroView.MeseroDetailView.as_view()),
    path('cliente/',clienteView.ClienteCreateView.as_view()),
    path('cliente/<int:pk>/',clienteView.ClienteDetailView.as_view()),
    path('cajero/',cajeroView.CajeroCreateView.as_view()),
    path('cajero/<int:pk>/',cajeroView.CajeroDetailView.as_view()),
     
]
