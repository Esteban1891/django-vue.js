from django.db import models

# Create your models here.

class Factura(models.Model):
    metodoPago = models.CharField(max_length=20, blank=False, default='')
    tipoComprobante = models.CharField(max_length=20,blank=False, default='')
    total = models.CharField(max_length=10,blank=False, default='')
    fecha = models.CharField(max_length=20,blank=False, default='')
    emisorNombre = models.CharField(max_length=80,blank=False, default='')
    emisorRFC = models.CharField(max_length=13,blank=False, default='')
    receptorNombre = models.CharField(max_length=80,blank=False, default='')
    receptorRFC = models.CharField(max_length=13,blank=False, default='')
    conceptoImporte = models.CharField(max_length=20,blank=False, default='')
    conceptoValor = models.CharField(max_length=20,blank=False, default='')
    conceptoDescripcion = models.CharField(max_length=80,blank=False, default='')
    impuestosTransImporte = models.CharField(max_length=20,blank=False, default='')
    impuestosTransTasa = models.CharField(max_length=20,blank=False, default='')
    impuestosTotalImp = models.CharField(max_length=20,blank=False, default='')