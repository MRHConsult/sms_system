from twilio.rest import Client

account_sid = 'ACe9ef99315219b935302494aa93d47288'
auth_token = 'd593eea60a59457dea08fe91f628283d'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MG99153bab8479e63191d9c74d3681bb05',
    body='How are you feeling today? Reply with 1: Good, 2: Not great',
    to='+27797983145',
)

print(message.status)