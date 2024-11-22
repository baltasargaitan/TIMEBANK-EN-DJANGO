from django.urls import path
from . import views
app_name='prestamos'
urlpatterns = [
    path('solicitar/', views.crear_prestamo, name='crear_prestamo'),
    path('listar/', views.listar_prestamos, name='listar_prestamos'),
    path('prestamos/<int:prestamo_id>/', views.detalle_prestamo, name='detalle_prestamo'),
]
