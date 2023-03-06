import os
import requests
import flight_search
import flight_data


# This class is responsible for talking to the Google Sheet.
class DataManager:

    def __init__(self):
        self.endpoint = os.environ.get('SHEETY_URL')
        self.token = os.environ.get('BEARER')
        self.headerz = {'Authorization': f'Bearer {self.token}'}

    def get_data(self):
        print('data_manager -> get_data called')
        # # call Sheety API to get cites you want to find cheap flights for within the next 6 months
        # requestor = requests.get(url=self.endpoint, headers=self.headerz)
        # requestor.raise_for_status()
        # # print(requestor.text)
        # payload = requestor.json()

        # testing payload
        payload = {
            "prices": [
                {
                    "city": "Paris",
                    "iataCode": "PAR",
                    "lowestPrice": "7000",
                    "id": 2
                },
                # {
                #     "city": "Berlin",
                #     "iataCode": "BER",
                #     "id": 3
                # },
                # {
                #     "city": "Houston",
                #     "iataCode": "IAH",
                #     "id": 4
                # },
                # {
                #     "city": "San Francisco",
                #     "iataCode": "SFO",
                #     "id": 5
                # },
                # {
                #     "city": "Auckland",
                #     "iataCode": "AKL",
                #     "id": 6
                # }
            ]
        }

        # find airports + flights for the cities returned from Sheety
        for x in payload['prices']:
            find_flights = flight_search.FlightSearch()
            find_flights.find_airport(x['city'])
            flight_payload = find_flights.get_flight_info(x['lowestPrice'])
            process_flight_data = flight_data.FlightData(flight_payload)
            process_flight_data.text_alert()

    def post_date(self, the_payload):
        post_to_sheety = requests.post(url=self.endpoint, json=the_payload, headers=self.headerz)
        post_to_sheety.raise_for_status()
        # print(post_to_sheety.text)

    pass
