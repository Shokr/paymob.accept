from random import *

from accept.payment import *

API_KEY = "<API-KEY>"
accept = AcceptAPI(API_KEY)


def test_retrieve_auth_token():
    auth_token = accept.retrieve_auth_token()
    assert len(auth_token) > 100


def test_order_registration():
    OrderData = {
        "auth_token": accept.retrieve_auth_token(),
        "delivery_needed": "false",
        "amount_cents": "1100",
        "currency": "EGP",
        "merchant_order_id": randint(1, 1000),
        "items": [
            {
                "name": "ASC1515",
                "amount_cents": "500000",
                "description": "Smart Watch",
                "quantity": "1"
            },
            {
                "name": "ERT6565",
                "amount_cents": "200000",
                "description": "Power Bank",
                "quantity": "1"
            }
        ],
        "shipping_data": {
            "apartment": "803",
            "email": "claudette09@exa.com",
            "floor": "42",
            "first_name": "Clifford",
            "street": "Ethan Land",
            "building": "8028",
            "phone_number": "+86(8)9135210487",
            "postal_code": "01898",
            "extra_description": "8 Ram , 128 Giga",
            "city": "Jaskolskiburgh",
            "country": "CR",
            "last_name": "Nicolas",
            "state": "Utah"
        },
        "shipping_details": {
            "notes": " test",
            "number_of_packages": 1,
            "weight": 10,
            "weight_unit": "Kilogram",
            "length": 100,
            "width": 100,
            "height": 100,
            "contents": "product of some sorts"
        }
    }
    order = accept.order_registration(OrderData)

    assert order.get("amount_cents") == 1100


def test_payment_key_request():
    OrderData = {
        "auth_token": accept.retrieve_auth_token(),
        "delivery_needed": "false",
        "amount_cents": "1100",
        "currency": "EGP",
        "merchant_order_id": randint(1, 1000),
        "items": [
            {
                "name": "ASC1515",
                "amount_cents": "500000",
                "description": "Smart Watch",
                "quantity": "1"
            },
            {
                "name": "ERT6565",
                "amount_cents": "200000",
                "description": "Power Bank",
                "quantity": "1"
            }
        ],
        "shipping_data": {
            "apartment": "803",
            "email": "claudette09@exa.com",
            "floor": "42",
            "first_name": "Clifford",
            "street": "Ethan Land",
            "building": "8028",
            "phone_number": "+86(8)9135210487",
            "postal_code": "01898",
            "extra_description": "8 Ram , 128 Giga",
            "city": "Jaskolskiburgh",
            "country": "CR",
            "last_name": "Nicolas",
            "state": "Utah"
        },
        "shipping_details": {
            "notes": " test",
            "number_of_packages": 1,
            "weight": 10,
            "weight_unit": "Kilogram",
            "length": 100,
            "width": 100,
            "height": 100,
            "contents": "product of some sorts"
        }
    }
    order = accept.order_registration(OrderData)

    Request = {
        "auth_token": accept.retrieve_auth_token(),
        "amount_cents": "1500",
        "expiration": 3600,
        "order_id": order.get("id"),
        "billing_data": {
            "apartment": "803",
            "email": "claudette09@exa.com",
            "floor": "42",
            "first_name": "Clifford",
            "street": "Ethan Land",
            "building": "8028",
            "phone_number": "+86(8)9135210487",
            "shipping_method": "PKG",
            "postal_code": "01898",
            "city": "Jaskolskiburgh",
            "country": "CR",
            "last_name": "Nicolas",
            "state": "Utah"
        },
        "currency": "EGP",
        "integration_id": 246701,  # https://accept.paymob.com/portal2/en/PaymentIntegrations
        "lock_order_when_paid": "false"
    }

    payment_token = accept.payment_key_request(Request)
    assert len(payment_token) > 100
