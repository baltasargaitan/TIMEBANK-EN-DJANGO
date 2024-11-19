from django.urls import path
from . import views
app_name='clientes'
urlpatterns = [
    path('listar/', views.listar_clientes, name='listar_clientes'),
    path('crear/', views.crear_cliente, name='crear_cliente'),
    path('<int:pk>/', views.detalle_cliente, name='detalle_cliente'),
]
