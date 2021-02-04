import json
import datetime
import requests

APIServer = 'https://test4.oamportal.com' 
access_token = None
 
#Retrieve access token (authentication)
def createToken():
    print("createToken")
    client_id = 'chalmers_test'
    client_secret = 'oWN3hmv9K6kYSGF96IP3pfWzrnk12Vo7'
    url = APIServer + "/oauth2/token"
    data = {
        'grant_type': 'client_credentials',
        'scope':'chargeportalservices'
    }

    response = requests.post(url, data=data, auth=(client_id,client_secret))
    #print(response.text)                           #debugging
    print(response)                                #debugging
    acc_response_json = response.json()             #Convert response to json object
    acc_token = acc_response_json["access_token"]   #Get the access token from the json object
    return(acc_token)

#Start Charger
def startCharger(token):
    print("startCharger")
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }

    data = '{"evseId":"d4ceb292-12ef-46b2-9724-0aeca7b62827","tagId":"[tag_id]", "transactionId":"00000000-0000-0000-0000-000000000000", "stoptime":"YYYY-MM-DDTHH:MM:SSZ"}'
    response = requests.post('https://test4.oamportal.com/ServicesApi/rest/charger/uuid/start', 
    headers=headers, data=data)
    print(response) #debugging
    

#Notify Start (request sent by charger)
def notifyStart(token): #funkar inte
    print("notifyStart")
    serverNotify = requests.get(APIServer + '/ServicesApi/rest/charger/uuid/start')
    if (serverNotify.status_code == 200):
        headers = {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json',
        }

        data = '{"accepted" : true,"errorCode" : "NO_ERROR"}'

        response = requests.post('https://test4.oamportal.com/ServicesApi/rest/charger/uuid/start', 
        headers=headers, data=data)
    else: 
        print(serverNotify)
        print(serverNotify.text)
access_token = createToken()
startCharger(access_token)
notifyStart(access_token)
#Stop Charger

#Notify Stop (request sent by charger)

#Change Active Current (amps)

#Consumed Energy (KWh) / duration

#Request Site Info
def requestSiteInfo():
    access_token = createToken()
    headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'application/json',
    }

    data = '{"siteid" : "6d411116-91cc-4a61-9b83-b83380a04e69"}'
    response = requests.post('https://test4.oamportal.com/ServicesApi/rest/charger/siteinfo', 
    headers=headers, data=data)
    print(response.text)

#Get Connector Status

#Set RFID tagID

#Request RFID tagID info

