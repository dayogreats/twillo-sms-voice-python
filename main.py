# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
import os
from twilio.rest import Client


# Set environment variables for your credentials
# Read more at http://twil.io/secure


# VOICE OPTION
class TwilioCall:

    def __init__(self):
        self.account_sid = "<account_sid>"
        self.auth_token = "<auth_token>"
        self.client = Client(self.account_sid, self.auth_token)

    def caller(self):
        call = self.client.calls.create(
            url="http://demo.twilio.com/docs/voice.xml",
            to="<to>",
            from_="<from>"
        )

        return call.sid


# SMS OPTION

class TwilioSMS:
    def __init__(self, account_sid, auth_token, from_number, to_number):
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number
        self.to_number = to_number

    def send_message(self, message):
        message = self.client.messages.create(
            from_=self.from_number,
            to=self.to_number,
            body=message
        )
        return message.sid


def main():
    # Use a breakpoint in the code line below to debug your script.
    # Make a call
    call = TwilioCall()
    call.caller()

    # Send Sms
    sms = TwilioSMS('<account_id>', '<account_token>', '<from>',
                    '<to>')
    sms.send_message('HelLo Bisi, Bayo ni o. Ku ojo ematu. Oko e ati awon omo e nko. Bami kiwon o')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
