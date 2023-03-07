import datetime

import notification_manager


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, payload):
        # flight dates
        self.take_off = payload['data'][0]['local_departure']
        # departure airport iata code
        self.depart_airport = payload['data'][0]['flyFrom']
        self.from_city = payload['data'][0]['cityFrom']
        # destination airport iata code
        self.destination_airport = payload['data'][0]['flyTo']
        self.to_city = payload['data'][0]['cityTo']
        # flight price
        self.flight_price = payload['data'][0]['price']
        # nights there
        self.nights_staying = payload['data'][0]['nightsInDest']
        # link to travel
        self.deep_link = payload['data'][0]['deep_link']

    def text_alert(self):
        takeoff = str.split(self.take_off,'T')
        return_date = datetime.datetime.strptime(takeoff[0],'%Y-%m-%d')
        return_date = return_date + datetime.timedelta(days=self.nights_staying)

        # print('flight_manager -> text_alert called')
        message = f'Low Price Alert: \n' \
                  f'Trip duration: {self.nights_staying}\n' \
                  f'Flight for 2 adults and 2 kids -> ${self.flight_price} USD\n' \
                  f'Take off date -> {takeoff[0]}\n' \
                  f'Return date -> {return_date.strftime("%Y-%m-%d")}\n' \
                  f'From: {self.from_city} -> {self.depart_airport}\n' \
                  f'To: {self.to_city} -> {self.destination_airport}\n' \
                  f''

        text_it = notification_manager.NotificationManager()
        print(f'message to be sent: \n {message}\n//////////////////////////////////////////\n\n')
        print('PRETEND YOU CALLED text_it.send_alert(message)')
        # text_it.send_alert(message)

    pass
