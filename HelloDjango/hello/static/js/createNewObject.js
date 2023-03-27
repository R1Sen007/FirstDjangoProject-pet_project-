function createNewObject() {
    
};


$(function(){
    $('#id_adress').prepend('<option value="">***Create new adress***</option>');
    $('#id_adress').change(function(){
        var value = $('#id_adress option:selected').text();
        

        if (value == "***Create new adress***") {
            window.location.href = "http://127.0.0.1:8000/shop/adress/create"
            // $.ajax({
            //     type: 'GET',
            //     url: 'http://127.0.0.1:8000/shop/adress/create',
            //     data: '',
            //     success: function(data) {
            //         var newWin = window.open("http://127.0.0.1:8000/shop/adress/create", "hello", "width=500,height=700");
            //         newWin.document.write(data);
            //     }
            // });
        }
    });
});

// $(function(){
//     $('#deleteButton').click(function(){
//         alert($('#deletePostForm').attr("action"))
//         // alert("hello")
//     });
// });


$('#deleteModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget)
    var recipient = button.data('pk') 
    var productName = button.data('pname')
    var deleteUrl = button.data('delete-url')
    //alert(deleteUrl)
    var modal = $(this)
    modal.find('.modal-body').text('Are you really want to delete: ' + productName + " ?")
    modal.find('.modal-footer form').attr("action", deleteUrl)
  })

