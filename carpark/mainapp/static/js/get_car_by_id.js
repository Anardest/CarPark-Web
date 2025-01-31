$(document).ready(function () {
    $('#get_car_by_id').click(function () {
        var carId = $("#carIdFind").val();
        $.ajax({
            type: "GET",
            url: "/get_car_by_id/" + carId + '/',
            success: function (response) {
                $('#car_info').empty();
                var carHtml = `
                <div class="d-flex justify-content-center" style="margin-top: 3rem;">
                    <div class="card">
                        <div class="card-body">
                            <h1 class="card-title">Автомобиль: ${response.make} ${response.model_name}</h1>
                            <p class="card-text">Id: ${response.id}</p>
                            <p class="card-text">Год выпуска: ${response.year}</p>
                            <p class="card-text">Пробег: ${response.mileage} км</p>
                            <p class="card-text">Количество поездок: ${response.trip_count}</p>
                            <a class="card-text" href="/cars/${response.slug}">Ссылка</a>
                        </div>
                    </div>
                </div>
                `;
                $('#car_info').html(carHtml)
            },
            error: function () {
                $('#car_info').html('<div class="alert alert-danger">Ошибка: Автомобиль не найден</div>');
            }
            
        })
    });
});