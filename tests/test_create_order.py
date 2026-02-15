import allure
import pytest
import requests

from url import URL
from data import DataForOrderScooter

@allure.title("когда создаёшь заказ можно указать один из цветов — BLACK или GREY, оба, не указывать цвет")
@pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
def test_create_order_color_scooter(color):
  data_col = DataForOrderScooter.ORDER_SCOOTER_DATA.copy()
  data_col["color"] = color

  response = requests.post(URL.CREATE_ORDER_ENDPOINT, json=data_col)

  assert response.status_code == 201
  assert "track" in response.json() 