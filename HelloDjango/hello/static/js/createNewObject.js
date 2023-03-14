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

