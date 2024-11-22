from django.urls import path
from . import views

app_name = 'transferencias'
urlpatterns = [
    path('crear/', views.crear_transferencia, name='crear_transferencia'),
    path('detalle/<int:transferencia_id>/', views.detalle_transferencia, name='detalle_transferencia'),
]
