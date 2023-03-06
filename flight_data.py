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

    def text_alert(self):
        print('flight_manager -> text_alert called')
        message = f'Low Price Alert: \n' \
                  f'Flight for 2 adults and 2 kids -> ${self.flight_price} USD' \
                  f'Take off date -> {self.take_off}\n' \
                  f'From: {self.from_city} -> {self.depart_airport}\n' \
                  f'To: {self.to_city} -> {self.destination_airport}\n'

        # print(message)
        text_it = notification_manager.NotificationManager()
        text_it.send_alert(message)

    pass
