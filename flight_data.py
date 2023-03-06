# If the price is lower than the lowest price listed in the Google Sheet then send an
# SMS to your own number with the Twilio API.

# The SMS should include the departure airport IATA code,
# destination airport IATA code, departure city, destination city,
# flight price and flight dates. e.g.


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, payload):
        # print(payload)
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

        # local_departure

    def text_alert(self):
        print('flight_manager -> text_alert called')
        message = f'Take off date -> {self.take_off}\n' \
                  f'{self.from_city} -> {self.depart_airport}\n' \
                  f'{self.to_city} -> {self.destination_airport}\n' \
                  f'Flight for 2 adults and 2 kids -> ${self.flight_price} USD'

        print(message)

    pass
