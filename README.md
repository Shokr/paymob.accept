# Paymob Accept Python Library

The Accept Python library provides convenient access to the Accept API from applications written in the Python language.
It includes a pre-defined set of classes for API resources that initialize themselves dynamically from API responses
which makes it compatible with a wide range of versions of the Accept API.

## Installation

```sh
pip install paymob.accept
```

Install from source with:

```sh
python setup.py install
```

### Requirements

- Python 3.4+

## Usage

The library needs to be configured with your account's secret key which is available in
your [Accept Dashboard](https://accept.paymob.com/portal2/en/settings).

Set `api_key` to its value:

```python

from accept.payment import *

API_KEY = "<API-KEY>"

accept = AcceptAPI(API_KEY)

# Authentication Request
auth_token = accept.retrieve_auth_token()
print(auth_token)

# Order Registration
OrderData = {
    "auth_token": auth_token,
    "delivery_needed": "false",
    "amount_cents": "1100",
    "currency": "EGP",
    "merchant_order_id": 125,  # UNIQUE
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
print(order)

# Payment Key Request
Request = {
    "auth_token": auth_token,
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
print(payment_token)

# Payments API [Kiosk, Mobile Wallets , Cash, Pay With Saved Token]
identifier = "cash"
payment_method = "CASH"
transaction = accept.pay(identifier, payment_method, payment_token)
print(transaction)

# Auth-Capture Payments
transaction00 = accept.capture_transaction(transaction_id="7608793", amount_cents=1000)
print(transaction00)

# Refund Transaction
transaction01 = accept.refund_transaction(transaction_id="7608793", amount_cents=10)
print(transaction01)

# Void Transaction
transaction02 = accept.void_transaction(transaction_id="7608793")
print(transaction02)

# Retrieve Transaction
transaction03 = accept.retrieve_transaction(transaction_id="7608793")
print(transaction03)

# Inquire Transaction
transaction_inquire = accept.inquire_transaction(merchant_order_id="123", order_id="10883471")
print(transaction_inquire)

# Tracking
order_10883471_track = accept.tracking(order_id="10883471")
print(order_10883471_track)

# Preparing Package
# This will return a pdf file url to be printed.
package = accept.preparing_package(order_id="10883471")  
print(package)

# IFrame URL
iframeURL = accept.retrieve_iframe(iframe_id="230796", payment_token=payment_token)
print(iframeURL)

# Loyalty Checkout
response = accept.loyalty_checkout(transaction_reference='', otp='123', payment_token=payment_token)
print(response)

```

