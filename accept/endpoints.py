class URLs:
    def __init__(self):
        self.base_url = "https://accept.paymob.com/api/"

        # auth
        self.auth = "auth/tokens"

        # ecommerce
        self.order = "ecommerce/orders"
        self.inquire_transaction = "ecommerce/orders/transaction_inquiry"
        self.tracking = "ecommerce/orders/{order_id}/delivery_status?token={token}".format(order_id="{order_id}",
                                                                                           token="{token}")
        self.preparing_package = "ecommerce/orders/{order_id}/airway_bill?token={token}".format(order_id="{order_id}",
                                                                                                token="{token}")

        # acceptance
        self.payment_key = "acceptance/payment_keys"
        self.payment = "acceptance/payments/pay"
        self.capture = "acceptance/capture"
        self.refund = "acceptance/void_refund/refund"
        self.void = "acceptance/void_refund/void?token={token}".format(token="{token}")
        self.retrieve_transaction = "acceptance/transactions/{id}?token={token}".format(id="{id}", token="{token}")
        self.loyalty_checkout = "acceptance/loyalty_checkout"
        self.iframe = "acceptance/iframes/{iframe_id}?payment_token={payment_token}".format(iframe_id="{iframe_id}",
                                                                                            payment_token="{payment_token}")

    def base_url(self):
        return self.base_url

    def authentication_url(self):
        return self.base_url + self.auth

    def order_registration_url(self):
        return self.base_url + self.order

    def payment_key_url(self):
        return self.base_url + self.payment_key

    def payment_url(self):
        return self.base_url + self.payment

    def capture_transaction_url(self):
        return self.base_url + self.capture

    def refund_transaction_url(self):
        return self.base_url + self.refund

    def void_transaction_url(self):
        return self.base_url + self.void

    def retrieve_transaction_url(self):
        return self.base_url + self.retrieve_transaction

    def inquire_transaction_with_order_details_url(self):
        return self.base_url + self.inquire_transaction

    def tracking_url(self):
        return self.base_url + self.tracking

    def preparing_package_url(self):
        return self.base_url + self.preparing_package

    def loyalty_checkout_url(self):
        return self.base_url + self.loyalty_checkout

    def iframe_url(self):
        return self.base_url + self.iframe
