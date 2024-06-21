# Софья Лукьянова, 17-я когорта — Финальный проект. Инженер по тестированию плюс
import senders_stand_request
import data


def test_create_and_get_order():
    # Шаг 1: Выполнить запрос на создание заказа
    response, track_number = senders_stand_request.post_new_order(data.order_body)

    # Проверка, что код ответа равен 201
    assert response.status_code == 201

    # Проверка, что трек-номер не None
    assert track_number is not None

    # Шаг 2: Выполнить запрос на получение заказа по треку заказа
    response = senders_stand_request.get_order(track_number)

    # Шаг 3: Проверить, что код ответа равен 200
    assert response.status_code == 200