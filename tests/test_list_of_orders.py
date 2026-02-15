import allure
import pytest
import requests

from url import URL

@allure.title("в тело ответа возвращается список заказов")
def test_ordlist_returned_in_response_body():
    response = requests.get(URL.ORDERS_LIST_ENDPOINT)

    assert response.status_code == 200
    assert "orders" in response.json()