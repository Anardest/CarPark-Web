$(document).ready(function () {
    $('#deleteDriverForm').on('submit', function(event) {
        event.preventDefault();

        var driverId = $('#driverIdDelete').val();
        $.ajax({
            type: 'POST',
            url: 'delete/driver/' + driverId + '/',
            data: {
                'driverIdDelete': driverId,
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()  // CSRF-токен
            },
            success: function(response) {
                $('#driverMessage').empty();
                let html = `<div class="alert alert-success">Водитель успешно удалён!</div>`;
                $('#driverMessage').html(html);
                $('#deleteDriverForm')[0].reset();
            },
            error: function(response) {
                $('#driverMessage').empty();
                let html = `<div class="alert alert-danger">Ошибка: ${response.responseJSON.error}</div>`;
                $('#driverMessage').html(html);
            }

        });
    });
});