from flask import redirect, request,Flask
from twilio.twiml.voice_response import VoiceResponse, Gather, Say
from twilio.rest import Client
import os
from models import details

app = Flask(__name__)
app.config['SECRET_KEY']='033dff7d4837f5d287dc53aad9946586'

data={}

@app.route("/home",methods=['GET','POST'])
def home():
    #return redirect("http://demo.twilio.com/docs/classic.mp3")
    response=VoiceResponse()
    gather = Gather(action='/process_address',input='speech')
    gather.say("Please tell your name")
    response.append(gather)
    response.say("We did not receive any input. Goodbye!")
    return str(response)

@app.route("/process_address",methods=['GET','POST'])
def process_address():
    data["Name"] = request.values["SpeechResult"]
    response=VoiceResponse()
    gather = Gather(action='/process_DOB',input='speech')
    gather.say("Please tell your address")
    response.append(gather)
    response.say("We did not receive any input. Goodbye!")
    return str(response)

@app.route("/process_DOB",methods=['GET','POST'])
def process_DOB():
    data["Address"] = request.values["SpeechResult"]
    response=VoiceResponse()
    gather = Gather(action='/store_details', numDigits="8",timeout="10")
    gather.say("Please type your DOB in day first, month number and year in left-to-right writing direction consisting of 8 digits.")
    response.append(gather)
    response.say("We did not receive any input. Goodbye!")
    return str(response)

@app.route("/store_details",methods=['GET','POST'])
def store_details():
    data["DOB"] = request.values["Digits"]
    details_df=details.append(data,ignore_index=True)
    print(details_df)
    response=VoiceResponse()
    response.say("Your details have been saved successfully. Thank you!")
    return str(response)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
