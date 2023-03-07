import twilio.rest
import os


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.sid = os.environ.get('ACCOUNT_SID')
        self.token = os.environ.get('AUTH_TOKEN')
        self.from_number = os.environ.get('TWILIO_NUMBER')
        self.to_number = os.environ.get('TARGET_PHONE_NUMBER')
        self.my_twillio = twilio.rest.Client(self.sid, self.token)

    def send_alert(self, message):
        print('Texting you the results now!')
        text_alert = self.my_twillio.messages.create(
            body=f"{message}",
            from_=os.environ.get('TWILIO_NUMBER'),
            to=os.environ.get('TARGET_PHONE_NUMBER'))

    pass
