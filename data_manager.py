import os
import requests
import flight_search


class DataManager:

    def __init__(self):
        self.endpoint = os.environ.get('SHEETY_URL')
        self.token = os.environ.get('BEARER')
        self.headerz = {'Authorization': f'Bearer {self.token}'}


    # This class is responsible for talking to the Google Sheet.
    def get_data(self):
        # requestor = requests.get(url=self.endpoint, headers=self.headerz)
        # requestor.raise_for_status()
        # print(requestor.text)
        # payload = requestor.json()

        # testing payload
        payload = {
          "prices": [
            {
              "city": "Paris",
              "iataCode": "PAR",
              "id": 2
            },
            {
              "city": "Berlin",
              "iataCode": "BER",
              "id": 3
            },
            {
              "city": "Houston",
              "iataCode": "IAH",
              "id": 4
            },
            {
              "city": "San Francisco",
              "iataCode": "SFO",
              "id": 5
            },
            {
              "city": "Auckland",
              "iataCode": "AKL",
              "id": 6
            }
          ]
        }

        for x in payload['prices']:
            # print(x['city'])
            # print(x['id'])
            find_airport = flight_search.FlightSearch()
            find_airport.find_airport(x['city'])

    def post_date(self, the_payload):
        post_to_sheety = requests.post(url=self.endpoint, json=the_payload, headers=self.headerz)
        post_to_sheety.raise_for_status()
        # print(post_to_sheety.text)

    pass
