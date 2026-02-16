import allure
import pytest
import requests

from helpers import register_new_courier_and_return_login_password
from url import URL
from generators import generate_fake_data

class TestLoginCourier:
    @allure.title("курьер может авторизоваться")
    def test_courier_auth(self):
        c_auth = register_new_courier_and_return_login_password() 
        payload = {
            "login": c_auth[0],
            "password": c_auth[1],
            }
        
        with allure.step("Отправка POST запроса на авторизацию курьера"):
            response = requests.post(URL.LOGIN_COURIER_ENDPOINT, data=payload)    

        with allure.step("Получение в ответе кода 200"):
           assert response.status_code == 200

        with allure.step("Получение в ответе id"):   
            assert "id" in response.json()

    @allure.title("система вернёт ошибку, если неправильно указать логин")
    def test_incorrect_login_fail(self):
        c_auth = register_new_courier_and_return_login_password()
        fake_login = generate_fake_data() 
        payload = {
            "login": fake_login["login"],
            "password": c_auth[1],
            }
        with allure.step("Отправка POST запроса на авторизацию курьера"):
            response = requests.post(URL.LOGIN_COURIER_ENDPOINT, data=payload)

        with allure.step("Получение в ответе кода 404"):
            assert response.status_code == 404

    @allure.title("если какого-то поля нет, запрос возвращает ошибку")
    def test_without_login_fail(self):    
        data = generate_fake_data()
        payload = {"password": data["password"]}

        with allure.step("Отправка POST запроса на авторизацию курьера"):
            response = requests.post(URL.LOGIN_COURIER_ENDPOINT, data=payload)

        with allure.step("Получение в ответе кода 400"):
            assert response.status_code == 400

        with allure.step("Получение сообщения об ошибке"):
            assert response.json() == { "message": "Недостаточно данных для создания учетной записи"}

    