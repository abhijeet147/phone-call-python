from twilio.rest import Client

account_sid = "your_account_sid"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

call = client.calls.create(
    to="receiver number",
    from_="sender number",
    url="http://demo.twilio.com/docs/voice.xml"
)

print("Call Started:", call.sid)
