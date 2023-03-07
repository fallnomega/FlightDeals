import twilio.rest
import os
import smtplib


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.sid = os.environ.get('ACCOUNT_SID')
        self.token = os.environ.get('AUTH_TOKEN')
        self.from_number = os.environ.get('TWILIO_NUMBER')
        self.to_number = os.environ.get('TARGET_PHONE_NUMBER')
        self.my_twillio = twilio.rest.Client(self.sid, self.token)
        self.user_email_address = ""
        self.test_email_address = os.environ.get('TEST_EMAIL')
        self.test_password = os.environ.get('TEST_PASSWORD')

    def send_alert(self, message):
        print('Texting you the results now!')
        text_alert = self.my_twillio.messages.create(
            body=f"{message}",
            from_=os.environ.get('TWILIO_NUMBER'),
            to=os.environ.get('TARGET_PHONE_NUMBER'))

    def email_users(self, message, email_list):
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.ehlo()
        connection.starttls()
        connection.login(user=self.test_email_address, password=self.test_password)
        for to_email in email_list:
            self.user_email_address = to_email
            connection.sendmail(from_addr=self.test_email_address,
                                to_addrs=self.user_email_address,
                                msg=f"{message}")
        connection.close()

    def test_email_users(self, message, email_list):
        print('TEST EMAILING CALLED')
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.ehlo()
        connection.starttls()
        connection.login(user=self.test_email_address, password=self.test_password)
        for to_email in email_list:
            self.user_email_address = to_email
            connection.sendmail(from_addr=self.test_email_address,
                                to_addrs=self.user_email_address,
                                msg=f"{message}")
        connection.close()

    pass
