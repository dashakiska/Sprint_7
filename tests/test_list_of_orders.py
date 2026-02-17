import allure
import pytest
import requests

from url import URL

class TestOrderList:
    @allure.title("в тело ответа возвращается список заказов")
    def test_ordlist_returned_in_response_body(self):

        with allure.step("Отправка GET запроса на получение списка заказов"):
            response = requests.get(URL.ORDERS_LIST_ENDPOINT)

        with allure.step("Получение в ответе кода 200"):
            assert response.status_code == 200

        with allure.step("Получение в ответе orders"):
            assert "orders" in response.json()