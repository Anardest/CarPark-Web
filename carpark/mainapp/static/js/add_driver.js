$(document).ready(function() {
    $('#driver-form').on('submit', function(event) {
        event.preventDefault();
        //console.log($(this).serialize());  // Отладка: выводим данные формы в консоль браузера

        $.ajax({
            url: '/add_driver/',
            type: 'POST',
            data: $(this).serialize(),
            success: function(response) {
                $('#driverMessage').html('<div class="alert alert-success">' + response.message + '</div>');
                $('#driver-form')[0].reset();
            },
            error: function(response) {
                $('#driverMessage').html('<div class="alert alert-danger">Ошибка: ' + response.responseJSON.error + '</div>');
            }
        });
    });
});