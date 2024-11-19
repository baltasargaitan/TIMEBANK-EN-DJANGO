from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_tarjetas, name='listar_tarjetas'),
    path('crear/', views.crear_tarjeta, name='crear_tarjeta'),
    path('<int:id>/', views.detalle_tarjeta, name='detalle_tarjeta'),
]
