import os
import requests


class DataManager:

    def __init__(self):
        self.endpoint = os.environ.get('SHEETY_URL')
        self.token = os.environ.get('BEARER')
        self.headerz = {'Authorization': f'Bearer {self.token}'}

        # test_payload = {
        #     "price":
        #         {
        #             "city": "San Francisco",
        #             "iataCode": "ZZ321",
        #             "lowestPrice": "20",
        #         }
        # }

    # This class is responsible for talking to the Google Sheet.
    def get_data(self):
        requestor = requests.get(url=self.endpoint, headers=self.headerz)
        requestor.raise_for_status()
        print(requestor.text)

    def post_date(self, the_payload):
        post_to_sheety = requests.post(url=self.endpoint, json=the_payload, headers=self.headerz)
        post_to_sheety.raise_for_status()
        print(post_to_sheety.text)

    pass
