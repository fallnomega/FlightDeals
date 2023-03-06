# This file will need to use the DataManager,FlightSearch,
# FlightData, NotificationManager classes to
# achieve the program requirements.

import data_manager
import flight_data
import flight_search
import notification_manager

my_sheety = data_manager.DataManager()
my_sheety.get_data()

# searching = flight_search.FlightSearch()
# searching.get_flight_info()


# TODO
# Program Requirements
# Use the Flight Search and Sheety API to populate your own copy of the Google Sheet
# with International Air Transport Association (IATA) codes for each city. Most of the
# cities in the sheet include multiple airports, you want the city code (not the airport code see here).


# If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.

# The SMS should include the departure airport IATA code, destination airport IATA code, departure city, destination city, flight price and flight dates. e.g.

