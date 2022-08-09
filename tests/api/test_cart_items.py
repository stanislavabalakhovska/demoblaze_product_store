import requests
import json

from data.endpoints import *
from data.constants import USER_NAME, USER_PASSWORD_ENCODE


def test_check_product_in_cart():
    user_data = {"username": USER_NAME, "password": USER_PASSWORD_ENCODE}
    headers = {"Content-Type": "application/json"}
    login_resp = requests.post(LOGIN_URL, data=json.dumps(user_data), headers=headers)
    assert login_resp.status_code == 200
    token = login_resp.json().replace('Auth_token: ', '')
    item = {
        "id": "61d34a55-0fc5-badf-f3f7-9045ebb3af14",
        "cookie": token,
        "prod_id": 3,
        "flag": False
    }
    r = requests.post(ADD_PRODUCT_TO_CART, data=json.dumps(item), headers=headers)
    assert r.status_code == 200
    data = {"cookie": token, "flag": True}
    r = requests.post(VIEW_CART_URL, data=json.dumps(data), headers=headers)
    assert r.status_code == 200
    items_in_cart = r.json().get("Items")
    assert len(items_in_cart) == 1
    assert items_in_cart[0]['prod_id'] == 3
    data = {"id": 3}
    r = requests.post(GET_PRODUCT_BY_ID, data=json.dumps(data), headers=headers)
    assert r.status_code == 200
    item_info = r.json()
    assert item_info['title'] == 'Nexus 6'
    assert int(item_info['price']) == 650
