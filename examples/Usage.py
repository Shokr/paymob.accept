from accept.payment import *

# These values are from Paymob.accept API.
API_KEY = "ZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6VXhNaUo5LmV5SnVZVzFsSWpvaWFXNXBkR2xoYkNJc0ltTnNZWE56SWpvaVRXVnlZMmhoYm5RaUxDSndjbTltYVd4bFgzQnJJam96TkRNemZRLkh0NS1VclIxS0t1N2MzVkIxbllMRGlYNUpTSy1jTWlKS1Vod1ExNnFGcmV2US05T3lvWDJUTnQyUm5saTZsMUZFblVVLVVPOThzS3p1MjgwVE92aXBn"

if __name__ == "__main__":
    accept = AcceptAPI(API_KEY)

    # Authentication Request
    print("-- Authentication Request --")

    auth_token = accept.retrieve_auth_token()
    print(auth_token)

    #################################################################################

    # Order Registration
    print("-- Order Registration --")

    OrderData = {
        "auth_token": auth_token,
        "delivery_needed": "false",
        "amount_cents": "1100",
        "currency": "EGP",
        "merchant_order_id": 125,
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

    #################################################################################

    # Payment Key Request
    print("-- Payment Key Request --")

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

    #################################################################################

    # Payments API [Kiosk, Mobile Wallets , Cash, Pay With Saved Token]
    print("-- Payments API --")

    identifier = "cash"
    payment_method = "CASH"

    transaction = accept.pay(identifier, payment_method, payment_token)

    print(transaction)

    #################################################################################

    # Auth-Capture Payments
    print("-- Auth-Capture Payments --")

    transaction00 = accept.capture_transaction("7608793", 1000)
    print(transaction00)

    #################################################################################

    # Refund Transaction
    print("-- Refund Transaction --")

    transaction01 = accept.refund_transaction("7608793", 10)
    print(transaction01)

    #################################################################################

    # Void Transaction
    print("-- Void Transaction --")

    transaction02 = accept.void_transaction("7608793")
    print(transaction02)

    #################################################################################

    # Retrieve Transaction
    print("-- Retrieve Transaction --")

    transaction03 = accept.retrieve_transaction("7608793")
    print(transaction03)

    #################################################################################

    # Inquire Transaction
    print("-- Inquire Transaction --")

    transaction_inquire = accept.inquire_transaction("123", "10883471")
    print(transaction_inquire)

    #################################################################################

    # Tracking
    print("-- Tracking --")

    order_10883471_track = accept.tracking("10883471")
    print(order_10883471_track)

    #################################################################################
    # This will return a pdf file to be printed.
    # Preparing Package
    print("-- Preparing Package --")

    package = accept.preparing_package("10883471")
    print(package)

    #################################################################################

    # IFrame URL
    print("-- IFrame URL --")

    iframeURL = accept.retrieve_iframe("230796", payment_token)
    print(iframeURL)
