function confirmarEliminacion(idPrograma) {
    Swal.fire({
        title: '¿Estas seguro?',
        text: "No podrás deshacer esta acción!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, eliminar',
        cancelButtonText:'Cancelar'
      }).then((result) => {
        if (result.isConfirmed) {
        
          window.location.href = "/eliminar-programa/"+idPrograma+"/";
        }
      })
}