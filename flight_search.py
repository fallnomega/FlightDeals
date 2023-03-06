import requests
import os
import datetime


# This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def __init__(self):
        # API doc - https://tequila.kiwi.com/portal/docs/tequila_api/search_api

        self.endpoint = os.environ.get('KIWI_URL')
        self.apikey = os.environ.get('KIWI_KEY')
        self.fly_from = 'SFO'
        self.fly_to = ''
        self.date_from = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        self.date_to = (datetime.datetime.today() + datetime.timedelta(weeks=24)).strftime('%d/%m/%Y')
        self.adults = 2
        self.children = 2
        self.selected_cabins = 'C'
        self.mix_with_cabins = 'M'
        self.adult_hold_bag = '1,1'
        self.adult_hand_bag = '1,1'
        self.child_hold_bag = '0,1'
        self.child_hand_bag = '1,0'
        self.currency = 'USD'
        self.price_to = 4000
        self.vehicle_type = 'aircraft'
        self.flight_type = 'oneway'

    # Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months
    # later for all the cities in the Google Sheet.

    def get_flight_info(self):
        print('flight_search -> get_flight_info called')
        parameters = {'fly_from': self.fly_from, 'fly_to': self.fly_to, 'date_from': self.date_from,
                      'date_to': self.date_to, 'max_fly_duration': 20,
                      'flight_type': self.flight_type, 'one_for_city': 0, 'one_per_date': 0, 'adults': self.adults,
                      'children': self.children, 'selected_cabins': self.selected_cabins,
                      'mix_with_cabins': self.mix_with_cabins,
                      'adult_hold_bag': self.adult_hold_bag, 'adult_hand_bag': self.adult_hand_bag,
                      'child_hold_bag': self.child_hold_bag, 'child_hand_bag': self.child_hand_bag,
                      'partner_market': 'us', 'curr': self.currency, 'max_stopovers': 2, 'max_sector_stopovers': 2,
                      'vehicle_type': self.vehicle_type, 'limit': 20}
        api = '/v2/search'
        headerz = {'accept': 'application/json', 'apikey': self.apikey}
        requestor = requests.get(headers=headerz, params=parameters,
                                 url=f'{self.endpoint}{api}'
                                 )
        print(requestor.url)
        requestor.raise_for_status()
        print(requestor.text)

    def find_airport(self, lookup_city):
        print('flight_search -> find_airport called')

        parameters = {'term': lookup_city, 'locale': 'en-US', 'location_types': 'airport', 'limit': 10,
                      'active_only': 'true'}
        headerz = {'accept': 'application/json', 'apikey': self.apikey}
        find_endpoint = '/locations/query'
        requestor = requests.get(url=f'{self.endpoint}{find_endpoint}', headers=headerz, params=parameters)
        requestor.raise_for_status()
        data_returned = requestor.json()
        airport_iata = data_returned["locations"][0]["id"]
        self.fly_to = airport_iata
        # print(f'{lookup_city} airport - {airport_iata}')
        # return airport_iata

    pass

# flightdealfinder
