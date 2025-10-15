from django.db import models

class Factura(models.Model):
    factura = models.CharField(max_length=20)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    cliente_id_cliente = models.IntegerField()
    proyecto_id_proyecto = models.IntegerField()

    def __str__(self):
        return f'Factura: {self.factura} - Monto: {self.monto}'
