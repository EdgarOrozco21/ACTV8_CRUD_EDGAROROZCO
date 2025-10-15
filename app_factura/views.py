from django.shortcuts import render, redirect, get_object_or_404
from .models import Factura

# Listar facturas
def index(request):
    facturas = Factura.objects.all()
    return render(request, 'listar_facturas.html', {'facturas': facturas})

# Ver factura
def ver_factura(request, id):
    factura = get_object_or_404(Factura, id=id)
    return render(request, 'ver_factura.html', {'factura': factura})

# Agregar factura
def agregar_factura(request):
    if request.method == 'POST':
        Factura.objects.create(
            factura=request.POST['factura'],
            fecha=request.POST['fecha'],
            monto=request.POST['monto'],
            metodo_pago=request.POST['metodo_pago'],
            cliente_id_cliente=request.POST['cliente_id_cliente'],
            proyecto_id_proyecto=request.POST['proyecto_id_proyecto']
        )
        return redirect('inicio')
    return render(request, 'agregar_factura.html')

# Editar factura
def editar_factura(request, id):
    factura = get_object_or_404(Factura, id=id)
    if request.method == 'POST':
        factura.factura = request.POST['factura']
        factura.fecha = request.POST['fecha']
        factura.monto = request.POST['monto']
        factura.metodo_pago = request.POST['metodo_pago']
        factura.cliente_id_cliente = request.POST['cliente_id_cliente']
        factura.proyecto_id_proyecto = request.POST['proyecto_id_proyecto']
        factura.save()
        return redirect('inicio')
    return render(request, 'editar_factura.html', {'factura': factura})

# Borrar factura
def borrar_factura(request, id):
    factura = get_object_or_404(Factura, id=id)
    if request.method == 'POST':
        factura.delete()
        return redirect('inicio')
    return render(request, 'borrar_factura.html', {'factura': factura})
