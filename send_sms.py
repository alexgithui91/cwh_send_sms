from twilio.rest import Client
from decouple import config

account_sid = config("ACCOUNT_SID")
auth_token = config("AUTH_TOKEN")

client = Client(account_sid, auth_token)

msg_body = "Coding With Hitz SMS Sent"

message = client.messages.create(
    from_=config("FROM_PHONE_NUMBER"),
    body=msg_body,
    to=config("TO_PHONE_NUMBER"),
)

print(message.sid)
