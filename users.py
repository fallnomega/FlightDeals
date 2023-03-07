import requests
import os


class User:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.email_address = ''
        self.endpoint = os.environ.get('USER_ADD')
        self.token = os.environ.get('BEARER')
        self.headerz = {'Authorization': f'Bearer {self.token}'}

    def register_user(self):
        self.first_name = input('Firstname:> ')
        self.last_name = input('Lastname:> ')
        email_mismatch = True
        while email_mismatch:
            self.email_address = input('Email Address:> ')
            retype_email_address = input('Email Address:> ')
            if self.email_address == retype_email_address:
                email_mismatch = False
                self.add_user()
                print("Added to the Flight Deal Club membership!")
            else:
                print("Email doesnt match, please provide and confirm your email address")

    def test_user(self):
        self.first_name = 'Jack'
        self.last_name = 'Johnson'
        self.email_address = 'testing@mywebsite.com'
        self.add_user()

    def add_user(self):

        print('users -> add_user called')
        data = {'user':
            {
                'firstName': self.first_name,
                'lastName': self.last_name,
                'email': self.email_address
            }
        }
        add_to_sheety = requests.post(url=self.endpoint, json=data, headers=self.headerz)
        add_to_sheety.raise_for_status()
        print(add_to_sheety.text)
