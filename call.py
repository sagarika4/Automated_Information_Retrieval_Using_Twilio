from twilio.rest import Client

account_sid = 'ACc95276005938b99730ac91a28fbf43c2'
auth_token = 'f10a7accd30e50d389b04ab8568af2ed'

client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='https://e0fd02db.ngrok.io/home',
                        to='+919899422124',
                        from_='+13347218490'
                    )
