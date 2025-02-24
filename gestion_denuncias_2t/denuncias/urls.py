from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_denuncias, name='lista_denuncias'),
    path('crear/', views.crear_denuncia, name='crear_denuncia'),
    path('editar/<int:id>/', views.editar_denuncia, name='editar_denuncia'),
    path('eliminar/<int:id>/', views.eliminar_denuncia, name='eliminar_denuncia'),
]