$(document).ready( function () {
    $('#datatable').DataTable({
        language: {

            search:         "Buscar",
            infoEmpty: "Sin resultado",
            zeroRecords: "Sin resultados encontrados",
            info: "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
            infoEmpty: "Mostrando 0 to 0 of 0 Entradas",
            infoFiltered: "(Filtrado de _MAX_ total entradas)",
            infoPostFix: "",
            paginate: {
                first:      "Primero",
                previous:    "Anterior",
                next:       "Siguiente"
            }
            },

            
        searchPanes:{
            
            dtOpts:{
                dom:'tp',
                searching:false
                
            }
          },
          dom: 'Pfrtip',
          columnDefs: [
          {
              searchPanes: {
                  show: true,
                  collapse:false
              },
              targets: [5]
          }],
    
  });
} );