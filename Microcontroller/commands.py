import json
import datetime
import requests

APIServer = 'https://test4.oamportal.com' 

#Retrieve access token (authentication)
def createToken():

    client_id = input("Username: ")
    client_secret = input("Password: ")
    url = APIServer + "/oauth2/token"
    data = {
        'grant_type': 'client_credentials',
        'scope':'chargeportalservices'
    }

    response = requests.post(url, data=data, auth=(client_id,client_secret))
    return response


#Start Charger

#Notify Start (request sent by charger)

#Stop Charger

#Notify Stop (request sent by charger)

#Change Active Current (amps)

#Consumed Energy (KWh) / duration

#Request Site Info

#Get Connector Status

#Set RFID tagID

#Request RFID tagID info

