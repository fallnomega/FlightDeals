import data_manager
import users

print('Welcome to Flight Deal Finder.\n'
      'Please provide us with your First Name, Last Name,\n'
      'and Email address to be added to the notification list.\n\n')
register_user = users.User()
# register_user.register_user()
# register_user.test_user()

my_sheety = data_manager.DataManager()
my_sheety.get_data()
