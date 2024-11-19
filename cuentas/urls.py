from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_cuentas, name='listar_cuentas'),
    path('crear/', views.crear_cuenta, name='crear_cuenta'),
    path('<int:id>/', views.detalle_cuenta, name='detalle_cuenta'),
]

