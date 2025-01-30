$(document).ready(function () {
    $('#get_driver_by_id').click(function () {
        var driverId = $('#driverIdFind').val();
        $.ajax({
            type: "GET",
            url: "/get_driver_by_id/" + driverId + '/',
            success: function (response) {
                $('#driver_info').empty();
                var driverHtml = `
                <div class="d-flex justify-content-center" style="margin-top: 3rem;">
                    <div class="card">
                        <div class="card-body">
                            <h1 class="card-title">Имя: ${response.name} ${response.surname}</h1>
                            <p class="card-text">Id: ${response.id}</p>
                            <p class="card-text">Год рождения: ${response.date_of_birth}</p>
                            <p class="card-text">Стаж: ${response.experience}</p>
                            <p class="card-text">Общее количество поездок: ${response.trip_count}</p>
                            <a class="card-text" href="/drivers/${response.slug}">Ссылка</a>
                        </div>
                    </div>
                </div>
                `;
                $('#driver_info').html(driverHtml);
            },
            error: function() {
                $('#driver_info').html('<p class="text-danger">Водитель не найден</p>');
            }
        });
    });
});