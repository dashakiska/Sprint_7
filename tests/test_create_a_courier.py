import allure
import pytest
import requests

from helpers import register_new_courier_and_return_login_password
from url import URL
from generators import generate_fake_data


@allure.title("Курьера можно создать")
def test_create_courier_success():
    new_courier = register_new_courier_and_return_login_password()
    assert len(new_courier) == 3


@allure.title("Нельзя создать двух одинаковых курьеров")
def test_create_two_identical_courier_fail():
    first_courier = register_new_courier_and_return_login_password()
    len(first_courier) == 3
    payload = {
        "login": first_courier[0],
        "password": first_courier[1],
        "firstName": first_courier[2]
    }
    response = requests.post(URL.CREATE_COURIER_ENDPOINT, data=payload)
    assert response.status_code == 409
    assert response.json() == {"message": "Этот логин уже используется"}

@allure.title("Создание курьера без обязательного поля логин")
def test_create_courier_without_login_fail():
    data = generate_fake_data()
    payload = {
        "password": data["password"],
        "firstName": data["firstName"]
    }

    response = requests.post(URL.CREATE_COURIER_ENDPOINT, data=payload)

    assert response.status_code == 400
    assert response.json() == {"message": "Недостаточно данных для создания учетной записи"}

@allure.title("Создание курьера. успешный запрос возвращает ok:true") 
def test_create_courier_status_true():
    data = generate_fake_data()
    payload = {
        "login": data["login"],
        "password": data["password"],
        "firstName": data["firstName"]
    }  

    response = requests.post(URL.CREATE_COURIER_ENDPOINT, data=payload)

    assert response.status_code == 201
    assert response.json() == {"ok": True}
      



