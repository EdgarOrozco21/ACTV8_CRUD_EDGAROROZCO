from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('<int:id>/', views.ver_factura, name='ver_factura'),
    path('agregar/', views.agregar_factura, name='agregar_factura'),
    path('editar/<int:id>/', views.editar_factura, name='editar_factura'),
    path('borrar/<int:id>/', views.borrar_factura, name='borrar_factura'),
]
