import requests


class PaystackApi:
    def __init__(self, secret_key):
        self.secret_key = secret_key
        self.url = 'https://api.paystack.co'

    def verify_transaction(self, transRef):
        response = requests.get(url=self.url + '/transaction/verify/' + transRef,
                                headers={"Authorization": f"Bearer {self.secret_key}"})
        return response.json()
