import allure
import pytest
import requests

from url import URL
from data import DataForOrderScooter

class TestCreateOrder:
    @allure.title("когда создаёшь заказ можно указать один из цветов — BLACK или GREY, оба, не указывать цвет")
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    
    def test_create_order_color_scooter(self, color):
        data_col = DataForOrderScooter.ORDER_SCOOTER_DATA.copy()
        data_col["color"] = color

        with allure.step("Отправка POST запроса на выбор цвета самоката"):
            response = requests.post(URL.CREATE_ORDER_ENDPOINT, json=data_col)

        with allure.step("Получение в ответе кода 201"):
            assert response.status_code == 201

        with allure.step("Получение в ответе track"):
            assert "track" in response.json() 