# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python, pip install twilio
from email import message
import os
from dotenv import load_dotenv
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
load_dotenv('.env')
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="",
    from_="",
    body="Hello there!")
