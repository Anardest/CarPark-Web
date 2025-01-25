$(document).ready(function() {
    $('#car-form').on('submit', function(event) {
        event.preventDefault();
        console.log('Форма отправлена');  // Отладка
        console.log($(this).serialize());  // Отладка

        $.ajax({
            url: '/add_car/',
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                console.log(response);  // Отладка
                $('#carMessage').html('<div class="alert alert-success">' + response.message + '</div>');
                $('#car-form')[0].reset();
            },
            error: function(response) {
                console.log(response);  // Отладка
                $('#carMessage').html('<div class="alert alert-danger">Ошибка: ' + response.responseJSON.error + '</div>');
            }
        });
    });
});