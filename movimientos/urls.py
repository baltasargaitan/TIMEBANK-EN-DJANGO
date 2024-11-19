from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_movimientos, name='listar_movimientos'),
    path('crear/', views.crear_movimiento, name='crear_movimiento'),
    path('<int:id>/', views.detalle_movimiento, name='detalle_movimiento'),
]
