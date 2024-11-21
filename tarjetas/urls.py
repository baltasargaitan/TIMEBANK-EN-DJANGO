from django.urls import path
from . import views
app_name = 'tarjetas'
urlpatterns = [
    path('listar/', views.listar_tarjetas, name='listar_tarjetas'),
    path('crear/', views.crear_tarjeta, name='crear_tarjeta'),
    path('<int:id>/', views.detalle_tarjeta, name='detalle_tarjeta'),
    path('<int:id>/eliminar/', views.eliminar_tarjeta, name='eliminar_tarjeta'),
]
