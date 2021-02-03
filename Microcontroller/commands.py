import json
import datetime
import requests

APIServer = 'https://test4.oamportal.com' 

#Retrieve access token (authentication)
def createToken():
    client_id = 'chalmers_test'
    client_secret = 'oWN3hmv9K6kYSGF96IP3pfWzrnk12Vo7'
    url = APIServer + "/oauth2/token"
    data = {
        'grant_type': 'client_credentials',
        'scope':'chargeportalservices'
    }

    response = requests.post(url, data=data, auth=(client_id,client_secret))
    print(response.text) #debugging
    return response.json.access_token

createToken()
#Start Charger
def startCharger():

    headers = {
        'Authorization': 'Bearer [access_token]',
        'Content-Type': 'application/json',
    }

    data = '{"evseId":"d4ceb292-12ef-46b2-9724-0aeca7b62827","tagId":"[tag_id]", "transactionId":"00000000-0000-0000-0000-000000000000", "stoptime":"YYYY-MM-DDTHH:MM:SSZ"}'

    response = requests.post('https://test4.oamportal.com/ServicesApi/rest/charger/uuid/start', 
    headers=headers, data=data)
    return response

#Notify Start (request sent by charger)

#Stop Charger

#Notify Stop (request sent by charger)

#Change Active Current (amps)

#Consumed Energy (KWh) / duration

#Request Site Info

#Get Connector Status

#Set RFID tagID

#Request RFID tagID info

