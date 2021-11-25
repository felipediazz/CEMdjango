$(document).ready( function () {
    $('#datatable').DataTable({
        dom: 'PBfrtip',

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
            },
            searchPanes: {
                clearMessage: 'Borrar selecciones',
                showMessage: 'Mostrar todos',
                collapseMessage: 'Ocultar todos',
                collapse: {0: 'Opciones de filtrado', _: 'Opciones de filtrado (%d)'},
                title: {
                    _: 'Filtros Seleccionados - %d',
                    0: 'Ningun filtro seleccionado',
                    1: 'Un filtro seleccionado'
                },
            
            }
            },
        responsive: "true",
            
        searchPanes:{
            cascadePanes: true,
            viewTotal: true,
            dtOpts:{
                dom:'tp',
                searching:false     
            }
          },
        buttons:[ 
			{
                extend:    'excelHtml5',
                text:      '<i class="fas fa-file-excel"></i> ',
                titleAttr: 'Exportar a Excel',
                className: 'btn btn-success'
            },
            {
                extend:    'pdfHtml5',
                text:      '<i class="fas fa-file-pdf"></i> ',
                titleAttr: 'Exportar a PDF',
                className: 'btn btn-danger'
            },
            {
                extend:    'print',
                text:      '<i class="fa fa-print"></i> ',
                titleAttr: 'Imprimir',
                className: 'btn btn-info'
            },
            {
                extend:    'copy',
                text:      '<i class="far fa-copy"></i>',
                titleAttr: 'Copiar',
                className: 'btn btn-primary'
            },
            {
                extend:    'csv',
                text:      '<i class="fas fa-file-csv"></i>',
                titleAttr: 'Exportar CSV',
                className: 'btn btn-warning'
            },
            
		],		
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


/*$(document).ready( function () {
    $('#datatable').DataTable({
        dom: 'Bfrtip',
        serverSide: false,
        stateSave: false,
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
            },
            searchPanes: {
                clearMessage: 'Borrar selecciones',
                showMessage: 'Mostrar todos',
                collapseMessage: 'Ocultar todos',
                collapse: {0: 'Opciones de filtrado', _: 'Opciones de filtrado (%d)'},
                title: {
                    _: 'Filtros Seleccionados - %d',
                    0: 'Ningun filtro seleccionado',
                    1: 'Un filtro seleccionado'
                }
            }
            },
            buttons: [
                {
                    extend: "searchPanes",
                    
                    text: '<i class="fas fa-file-csv"></i>',
                    titleAttr: 'Paneles de busqueda',
                    config: {
                        layout: "columns-2",
                        cascadePanes: true
                        
                    },
                    className: 'btn btn-dark'
                },
                {
                    extend:    'excelHtml5',
                    text:      '<i class="fas fa-file-excel"></i> ',
                    titleAttr: 'Exportar a Excel',
                    className: 'btn btn-success'
                },
                {
                    extend:    'pdfHtml5',
                    text:      '<i class="fas fa-file-pdf"></i> ',
                    titleAttr: 'Exportar a PDF',
                    className: 'btn btn-danger'
                },
                {
                    extend:    'print',
                    text:      '<i class="fa fa-print"></i> ',
                    titleAttr: 'Imprimir',
                    className: 'btn btn-info'
                },
                {
                    extend:    'copy',
                    text:      '<i class="far fa-copy"></i>',
                    titleAttr: 'Copiar',
                    className: 'btn btn-primary'
                },
                {
                    extend:    'csv',
                    text:      '<i class="fas fa-file-csv"></i>',
                    titleAttr: 'Exportar CSV',
                    className: 'btn btn-warning'
                },
            ]
    
  });
} );
*/