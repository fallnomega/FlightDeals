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
        # print('data_manager -> get_data called')
        # call Sheety API to get cites you want to find cheap flights for within the next 6 months
        requestor = requests.get(url=self.endpoint, headers=self.headerz)
        requestor.raise_for_status()
        payload = requestor.json()

        # # testing payload
        # payload = {
        #     "prices": [
        #         {
        #             "city": "Paris",
        #             "iataCode": "CDG",
        #             "lowestPrice": "20000",
        #             "id": 2
        #         },
        #         {
        #             "city": "Bali",
        #             "iataCode": "DPS",
        #             "lowestPrice": "20000",
        #             "id": 3
        #         },
        #         {
        #             "city": "Houston",
        #             "iataCode": "HOU",
        #             "lowestPrice": "20000",
        #             "id": 4
        #         },
        #         {
        #             "city": "Auckland",
        #             "iataCode": "AKL",
        #             "lowestPrice": "20000",
        #             "id": 5
        #         },
        #         {
        #             "city": "Asheville",
        #             "iataCode": "AVL",
        #             "lowestPrice": "20000",
        #             "id": 6
        #         }
        #     ]
        # }

        # find airports + flights for the cities returned from Sheety
        for x in payload['prices']:
            find_flights = flight_search.FlightSearch()
            destination_iata = find_flights.find_airport(x['city'])
            print(f"Finding flights to {x['city']} in the best William Shatner impersonation I can muster.")
            if x['iataCode'] == '':
                self.update_data(destination_iata, x)
            try:
                flight_payload = find_flights.get_flight_info(x['lowestPrice'])
                process_flight_data = flight_data.FlightData(flight_payload)
            except IndexError as error:
                print(f"No flights found, looking for one with a stop over.")
                try:
                    find_flights.max_stopovers = 2
                    flight_payload = find_flights.get_flight_info(x['lowestPrice'])
                    find_flights.via_city = flight_payload['data'][0]['route'][1]['flyFrom']
                    process_flight_data = flight_data.FlightData(flight_payload,
                                                                 stops=flight_payload['data'][0]['route'][1]['flyFrom'])

                except:
                    print(f"Still no flights found.Exiting program")
                    exit()
                else:
                    process_flight_data.text_alert()
                    process_flight_data.email_alert()

            else:
                # print('DOING THINGS FOR TESTING PURPOSES')
                process_flight_data.text_alert()
                process_flight_data.email_alert()

    def update_data(self, iata, item):
        # print('data_manager -> post_data called')
        data = {
            'price': {
                'city': item['city'],
                'lowestPrice': item['lowestPrice'],
                'iataCode': iata}
        }
        endpoint = f'{self.endpoint}/{item["id"]}'
        # requests.put(url, params={key: value}, args)
        post_to_sheety = requests.put(url=endpoint, json=data, headers=self.headerz)
        post_to_sheety.raise_for_status()

    pass
