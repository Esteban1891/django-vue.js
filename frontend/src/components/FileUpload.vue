<template>
  <div id="file-upload">
    <hr />
    <h1>1.- Cargar archivo XML</h1>

    

    <input type="file" style="" @change="readFileAsJson" accept=".xml" />
    <br /><br />
    <button
      type="button"
      v-show="showFile"
      @click="sendInvoice"
      class="btn btn-success"
    >
      Guardar Factura
    </button>
    <br><br>
    <div v-show="showData">
     <div class="alert alert-success alert-dismissible fade show" role="alert">
      <strong>¡Registro Exitoso!</strong> La factura se guardo correctamente.
       <button type="button" class="close" data-dismiss="alert" aria-label="Close">
      <span aria-hidden="true">&times;</span>
      </button>
     </div>
    </div>
    <div v-show="showDataError">
     <div class="alert alert-danger alert-dismissible fade show" role="alert">
      <strong>¡Error!</strong> La factura no se pudo guardar correctamente, consulte al administrador.
       <button type="button" class="close" data-dismiss="alert" aria-label="Close">
      <span aria-hidden="true">&times;</span>
      </button>
     </div>
    </div>

    <br />
    <div v-show="showData">
      <hr />
      <h1>2.- Obtener datos registrados en base de datos</h1>
      <button
        type="button"
        v-show="showData"
        @click="getInvoices"
        class="btn btn-success"
      >
        Consultar Facturas
      </button>
      <br /><br />

      <div>
        <table class="table table-striped">
          <thead>
            <tr v-show="showDataH">
              <th scope="col">M.Pago</th>
              <th scope="col">T.Comp</th>
              <th scope="col">Total</th>
              <th scope="col">Fecha</th>
              <th scope="col">E.Nombre</th>
              <th scope="col">E.RFC</th>
              <th scope="col">R.Nombre</th>
              <th scope="col">R.RFC</th>
              <th scope="col">C.Imp</th>
              <th scope="col">C.ValUni</th>
              <th scope="col">C.Des</th>
              <th scope="col">I.TraImp</th>
              <th scope="col">I.TraTas</th>
              <th scope="col">I.TotImp</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="dat in invoices" v-bind:key="dat.id">
              <td>{{ dat.metodoPago }}</td>
              <td>{{ dat.tipoComprobante }}</td>
              <td>{{ dat.total }}</td>
              <td>{{ dat.fecha }}</td>
              <td>{{ dat.emisorNombre }}</td>
              <td>{{ dat.emisorRFC }}</td>
              <td>{{ dat.receptorNombre }}</td>
              <td>{{ dat.receptorRFC }}</td>
              <td>{{ dat.conceptoImporte }}</td>
              <td>{{ dat.conceptoValor }}</td>
              <td>{{ dat.conceptoDescripcion }}</td>
              <td>{{ dat.impuestosTransImporte }}</td>
              <td>{{ dat.impuestosTransTasa }}</td>
              <td>{{ dat.impuestosTotalImp }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import xmljs from "xml-js";

export default {
  name: "FileUpload",
  data() {
    return {
      showData: false,
      showDataError: false,
      showDataH: false,
      showFile: false,
      invoices: null,
      xml: null,
      json: null
    };
  },
  mounted() {},
  methods: {
    getInvoices: function () {
      axios
        .get("http://localhost:8000/api/getFacturaxion/")
        .then((response) => {
          this.showDataH = true;
          this.invoices = response.data;
        })
        .catch((e) => console.log(e));
    },
    sendInvoice: function () {
      axios
        .post("http://localhost:8000/api/createFacturaxion/", this.json)
        .then((response) => {
           console.info(response)
        })
        .catch((e) => console.log(e));

      this.showData = true;
    },
    readFileAsJson: function (event) {
      this.showFile = true;

      let file = event.target.files[0];
      let reader = new FileReader();

      reader.readAsText(file, "windows-1251");
      reader.onload = () => {
        const xmltojson = xmljs.xml2js(reader.result);
        this.parseXMLtoJSON(xmltojson);
      };
    },
    parseXMLtoJSON: function (json) {

      this.json = {
        metodoPago: json.elements[0].attributes.MetodoPago,
        tipoComprobante: json.elements[0].attributes.TipoDeComprobante,
        total: json.elements[0].attributes.Total,
        fecha: json.elements[0].attributes.Fecha,
        emisorNombre: json.elements[0].elements[0].attributes.Nombre,
        emisorRFC: json.elements[0].elements[0].attributes.Rfc,
        receptorNombre: json.elements[0].elements[1].attributes.Nombre,
        receptorRFC: json.elements[0].elements[1].attributes.Rfc,
        conceptoImporte: json.elements[0].elements[2].elements[0].attributes.Importe,
        conceptoValor: json.elements[0].elements[2].elements[0].attributes.ValorUnitario,
        conceptoDescripcion: json.elements[0].elements[2].elements[0].attributes.Descripcion,
        impuestosTransImporte: json.elements[0].elements[3].attributes.TotalImpuestosTrasladados,
        impuestosTransTasa: json.elements[0].elements[3].elements[0].elements[0].attributes.TasaOCuota,
        impuestosTotalImp: json.elements[0].elements[3].elements[0].elements[0].attributes.Importe,
      };
    },
  },
};
</script>
