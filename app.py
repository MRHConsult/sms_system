from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.form['Body']

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == '1':
        resp.message("Hi!, Great to hear that. Continue to have a great day!")
    elif body == '2':
        resp.message("Hi! We are sorry to hear that. But we are here for you! Call this number: 0800 000 000 to speak "
                     "to our specialist.")
    else:
        resp.message('How are you feeling today? Reply with 1: Good, 2: Not great')
    return str(resp)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
