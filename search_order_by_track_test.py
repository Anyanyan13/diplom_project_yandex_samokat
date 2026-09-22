# Анна Ларченкова, 47-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

def get_order_body(firstName, lastName, address, metroStation, phone, rentTime, deliveryDate, comment, color):    # добавление данных для создания нового заказа
    current_order_body = data.order_body.copy()
    current_order_body["firstName"] = firstName
    current_order_body["lastName"] = lastName
    current_order_body["address"] = address
    current_order_body["metroStation"] = metroStation
    current_order_body["phone"] = phone
    current_order_body["rentTime"] = rentTime
    current_order_body["deliveryDate"] = deliveryDate
    current_order_body["comment"] = comment
    current_order_body["color"] = color
    return current_order_body

def check_code(body):                                                                                               
    track_number = sender_stand_request.create_new_order(body).json()["track"]                              # отправка запроса на создание заказа и сохранение вернувшегося трек-номера в переменную
    search_response = sender_stand_request.search_order_by_track(track_number)                              # отправка запроса на получение заказа по треку заказа
    assert search_response.status_code == 200                                                               # проверка , что код ответа равен 200

def test_search_new_order_by_track():
    new_params = get_order_body("Анна", "Петрова", "ул. Освобождения, 2-23.", 4, "89001112233", 1, "2026-09-20", "После 11-00, утром.", ["BLACK"])
    check_code(new_params)
