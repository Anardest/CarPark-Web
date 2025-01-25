$(document).ready(function() {
    // Обработчик для кнопки "Показать автомобили"
    $('#show-cars').click(function() {
        $.get('/get_cars/', function(data) {
            // Показываем таблицу автомобилей и скрываем остальные
            $('#cars-table').show();
            $('#drivers-table').hide();
            $('#trips-table').hide();

            // Очищаем содержимое tbody
            $('#cars-table-body').empty();

            // Перебираем данные и создаём строки таблицы
            data.forEach(function(car) {
                let row = `
                    <tr>
                        <td>${car.make}</td>
                        <td>${car.model_name}</td>
                        <td>${car.year}</td>
                        <td>${car.mileage} км</td>
                        <td><a href="/cars/${car.slug}/">Подробнее</a></td>
                    </tr>
                `;
                $('#cars-table-body').append(row);
            });
        });
    });

    // Обработчик для кнопки "Показать водителей"
    $('#show-drivers').click(function() {
        $.get('/get_drivers/', function(data) {
            // Показываем таблицу водителей и скрываем остальные
            $('#drivers-table').show();
            $('#cars-table').hide();
            $('#trips-table').hide();

            // Очищаем содержимое tbody
            $('#drivers-table-body').empty();

            // Перебираем данные и создаём строки таблицы
            data.forEach(function(driver) {
                let row = `
                    <tr>
                        <td>${driver.surname}</td>
                        <td>${driver.name}</td>
                        <td>${driver.date_of_birth}</td>
                        <td><a href="/drivers/${driver.slug}/">Подробнее</a></td>
                    </tr>
                `;
                $('#drivers-table-body').append(row);
            });
        });
    });

    // Обработчик для кнопки "Показать поездки"
    $('#show-trips').click(function() {
        $.get('/get_trips/', function(data) {
            // Показываем таблицу поездок и скрываем остальные
            $('#trips-table').show();
            $('#cars-table').hide();
            $('#drivers-table').hide();

            // Очищаем содержимое tbody
            $('#trips-table-body').empty();

            // Перебираем данные и создаём строки таблицы
            data.forEach(function(trip) {
                let row = `
                    <tr>
                        <td>${trip.start_point}</td>
                        <td>${trip.end_point}</td>
                        <td>${trip.driver_id__surname} ${trip.driver_id__name}</td>
                        <td>${trip.car_id__make} ${trip.car_id__model_name}</td>
                        <td>${trip.start_time}</td>
                        <td>${trip.end_time}</td>
                        <td><a href="/trips/${trip.slug}/">Подробнее</a></td>
                    </tr>
                `;
                $('#trips-table-body').append(row);
            });
        });
    });
});