from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    number = request.values.get('from', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == '2':
        resp.message("Hi! We are sorry to hear that. But we are hear for you. Call this number: 0800 000 000 to speak "
                     "to our specialist.")
    elif body == '1':
        resp.message("Hi!, Great to hear that. Continue to have a great day!")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)