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
        self.fly_to = 'BER'
        self.date_from = '04/04/2023'
        self.date_to = '05/04/2023'
        self.return_from = '06/04/2023'
        self.return_to = '07/04/2023'
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

    def get_flight_info(self):
        params = {'apikey': self.apikey, 'fly_from': self.fly_from, 'fly_to': self.fly_to, 'date_from': self.date_from,
                  'date_to': self.date_to}  # , 'adults': self.adults, 'children': self.children
        api = '/v2/search'
        headerz = {'accept': 'application/json','apikey': self.apikey}
        # requestor = requests.get(url=f"{self.endpoint}{api}",params=params)
        requestor = requests.get( headers=headerz,
            url=f'https://api.tequila.kiwi.com/v2/search?fly_from={self.fly_from}&fly_to={self.fly_to}'
                f'&date_from={self.date_from}&date_to={self.date_to}&return_from={self.return_from}'
                f'&return_to={self.return_to}&flight_type=round&adults={self.adults}&children={self.children}'
                f'&selected_cabins={self.selected_cabins}&mix_with_cabins={self.mix_with_cabins}'
                f'&adult_hold_bag={self.adult_hold_bag}&adult_hand_bag={self.adult_hand_bag}'
                f'&child_hold_bag={self.child_hold_bag}&child_hand_bag={self.child_hand_bag}'
                f'&partner_market=us&curr=USD&max_stopovers=2&max_sector_stopovers=2&vehicle_type=aircraft&limit=500' \
)
        print(requestor.url)
        requestor.raise_for_status()
        print(requestor.text)

    pass

# flightdealfinder
