import allure
import pytest
import requests

from helpers import register_new_courier_and_return_login_password
from url import URL
from generators import generate_fake_data

@allure.title("курьер может авторизоваться")
def test_courier_auth():
    c_auth = register_new_courier_and_return_login_password() 
    payload = {
        "login": c_auth[0],
        "password": c_auth[1],
        }
    
    response = requests.post(URL.LOGIN_COURIER_ENDPOINT, data=payload)    

    assert response.status_code == 200
    assert "id" in response.json()

@allure.title("система вернёт ошибку, если неправильно указать логин")
def test_incorrect_login_fail():
    c_auth = register_new_courier_and_return_login_password()
    fake_login = generate_fake_data() 
    payload = {
        "login": fake_login["login"],
        "password": c_auth[1],
        }
    
    response = requests.post(URL.LOGIN_COURIER_ENDPOINT, data=payload)

    assert response.status_code == 404

@allure.title("если какого-то поля нет, запрос возвращает ошибку")
def test_without_login_fail():    
    data = generate_fake_data()
    payload = {"password": data["password"]}

    response = requests.post(URL.LOGIN_COURIER_ENDPOINT, data=payload)

    assert response.status_code == 400
    assert response.json() == { "message": "Недостаточно данных для создания учетной записи"}

    