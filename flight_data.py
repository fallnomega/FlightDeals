import datetime

import notification_manager
import users


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, payload, stops="0"):
        # overall_data
        self.overall_data = payload
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
        # stop overs
        self.stop_over = stops

    def text_alert(self):
        takeoff = str.split(self.take_off, 'T')
        return_date = datetime.datetime.strptime(takeoff[0], '%Y-%m-%d')
        return_date = return_date + datetime.timedelta(days=self.nights_staying)

        # print('flight_manager -> text_alert called')
        message = f'Low Price Alert: \n' \
                  f'Trip duration: {self.nights_staying}\n' \
                  f'Flight for 2 adults and 2 kids -> ${self.flight_price} USD\n' \
                  f'Take off date -> {takeoff[0]}\n' \
                  f'Return date -> {return_date.strftime("%Y-%m-%d")}\n' \
                  f'From: {self.from_city} -> {self.depart_airport}\n' \
                  f'To: {self.to_city} -> {self.destination_airport}\n' \
                  f'Stop over: {self.stop_over}'

        text_it = notification_manager.NotificationManager()
        text_it.send_alert(message)

    def compose_email(self):
        takeoff = str.split(self.take_off, 'T')
        return_date = datetime.datetime.strptime(takeoff[0], '%Y-%m-%d')
        return_date = return_date + datetime.timedelta(days=self.nights_staying)
        return_date = return_date.date()
        takeoff = takeoff[0]

        link = f"https://www.google.com/flights?hl=en#flt={self.overall_data['data'][0]['flyFrom']}." \
               f"{self.overall_data['data'][0]['flyTo']}.{takeoff}*{self.overall_data['data'][0]['flyTo']}." \
               f"{self.overall_data['data'][0]['flyFrom']}.{return_date}"
        message = f"Low price alert! Only ${self.flight_price} USD to fly from {self.overall_data['data'][0]['cityFrom']}-" \
                  f"{self.overall_data['data'][0]['flyFrom']} to {self.overall_data['data'][0]['cityTo']}-" \
                  f"{self.overall_data['data'][0]['flyTo']}, from {takeoff} to {return_date}.\n" \
                  f"{link}"

        return message

    def email_alert(self):
        email_of_users = users.User()
        the_list = email_of_users.get_email()
        email_it = notification_manager.NotificationManager()
        message = self.compose_email()
        email_it.email_users(message=message, email_list=the_list)
        print(f'Text Message and Email Sent!\n//////////////////////////////////////////\n\n')

    pass
