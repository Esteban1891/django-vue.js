from rest_framework import serializers
from apps.facturaxion.models import Factura


class FacturaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Factura
        fields = ('id',
                  'metodoPago',
                  'tipoComprobante',
                  'total',
                  'fecha',
                  'emisorNombre',
                  'emisorRFC',
                  'receptorNombre',
                  'receptorRFC',
                  'conceptoImporte',
                  'conceptoValor',
                  'conceptoDescripcion',
                  'impuestosTransImporte',
                  'impuestosTransTasa',
                  'impuestosTotalImp'
                  )
