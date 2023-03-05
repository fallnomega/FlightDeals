import requests
import os
import datetime


# This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def __init__(self):
        # API doc - https://tequila.kiwi.com/portal/docs/tequila_api/search_api

        self.endpoint = os.environ.get('KIWI_URL')
        self.apikey = os.environ.get('KIWI_KEY')
        self.fly_from = 'OAK,SFO'
        self.fly_to = ''
        self.date_from = ''
        self.date_to = ''
        self.return_from = ''
        self.return_to = ''
        self.adults = 2
        self.children = 2
        self.selected_cabins = ''
        self.adult_hold_bag = ''
        self.adult_hand_bag = ''
        self.child_hold_bag = ''
        self.child_hand_bag = ''
        self.curr = 'USD'
        self.price_to = 4000

    def get_flight_info(self):
        params = {'apikey':self.apikey,'fly_from': self.fly_from, 'fly_to': self.fly_to, 'date_from': self.date_from,
                  'date_to': self.date_to, 'adults': self.adults, 'children': self.children}

    pass

# flightdealfinder
