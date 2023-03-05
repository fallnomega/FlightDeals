import os
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    url = os.environ.get('SHEETY_URL')
    token = os.environ.get('BEARER')

    # # sheet columns
    # City,IATA Code,Lowest Price

    pass
