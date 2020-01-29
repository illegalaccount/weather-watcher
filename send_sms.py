from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_baby, my_twilio
import weather

client = Client(account_sid, auth_token)

my_msg = weather.get_weather()
message = client.messages \
                .create(
                     body=my_msg,
                     from_=my_twilio,
                     to=my_baby
                 )

print(message.sid)