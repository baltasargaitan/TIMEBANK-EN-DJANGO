from django.urls import path
from . import views
app_name='clientes'
urlpatterns = [
    path('cliente/<int:cliente_id>/', views.ver_cliente, name='ver_cliente'),
    path('completar_perfil/', views.completar_perfil, name='completar_perfil'),
]
