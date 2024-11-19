from django.urls import path
from . import views

urlpatterns = [
    path('solicitar/', views.solicitar_prestamo, name='solicitar_prestamo'),
    path('listar/', views.listar_prestamos, name='listar_prestamos'),
    path('<int:id>/', views.detalle_prestamo, name='detalle_prestamo'),
]
