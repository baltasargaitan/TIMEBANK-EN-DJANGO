from . import views
from django.urls import path
app_name='homebanking'
urlpatterns = [
    path("", views.index, name='homebanking'),
]