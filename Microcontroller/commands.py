import json
import datetime
import requests

APIServer = 'https://test4.oamportal.com' 
 
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
    print(response)                                 #debugging
    acc_response_json = response.json()             #Convert response to json object
    acc_token = acc_response_json["access_token"]   #Get the access token from the json object
    return(acc_token)                               #Return the access token so that it can be used later

#Start Charger
#Send the request to activate the connector on the charge station
#TODO:
#Add stoptime
def startCharger(token,transactionId):
    print("startCharger")
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }

    data = '{"evseId":"d4ceb292-12ef-46b2-9724-0aeca7b62827","tagId":"[tag_id]", "transactionId":' +transactionId+', "stoptime":"YYYY-MM-DDTHH:MM:SSZ"}'
    response = requests.post('https://test4.oamportal.com/ServicesApi/rest/charger/uuid/start', 
    headers=headers, data=data)
    print(data)
    print(response)
    

#Notify Start (request sent by charger)
#Server response

#Stop Charger
def stopCharger(token,transactionID):
    print("stopCharger")
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }

    data = '{"evseId" : "d4ceb292-12ef-46b2-9724-0aeca7b62827", "transactionId" :' +transactionID+'}'
    response = requests.post('https://test4.oamportal.com/ServicesApi/rest/charger/uuid/stop', 
    headers=headers, data=data)
    print(data)
    print(response)

#Notify Stop (request sent by charger)
#Server Response

#Change Active Current (amps)
#TODO:
#Add input from optimisation model
def changeActiveCurrent(token):
    print("changeActiveCurrent")
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }

    data = '{"current": "[current]", "chargeboxidentity": "000005354-1","connectorid": "1"}'

    response = requests.post('https://test4.oamportal.com/ServicesApi/rest/charger/changeactivecurrent', 
    headers=headers, data=data)
    print(response)
    print(response.text)
    
#Consumed Energy (KWh) / duration
def consumedEnergy(token):
    print("consumedEnergy")
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }

    data = '{"tagId" : "[tag_id]", "intervalStart" : "YYYY-MM-DD"," intervalEnd" : "YYYY-MM-DD"}'

    response = requests.post('https://test4.oamportal.com/ServicesApi/rest/tag/getSessionsByTag', 
    headers=headers, data=data)
    print(response)
    print(response.text)

#Request Site Info
def requestSiteInfo(token):
    print("requestSiteInfo")
    headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json',
    }

    data = '{"siteid" : "6d411116-91cc-4a61-9b83-b83380a04e69"}'
    response = requests.post('https://test4.oamportal.com/ServicesApi/rest/charger/siteinfo', 
    headers=headers, data=data)
    print(response)
    print(response.text)

#Get Connector Status
def connectorStatus(token):
    print("connectorStatus")
    headers = {
        'Authorization': 'Bearer ' + token,
    }

    response = requests.get('https://test4.oamportal.com/ServicesApi/rest/charger/status/d4ceb292-12ef-46b2-9724-0aeca7b62827', 
    headers=headers)
    print(response)
    print(response.text)

#Set RFID tagID
def setRFIDtagID(token):
    print("setRFIDtagID")
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }

    data = '{"tagId":"918273645","companyId":170401,"validTo" : "YYYY-MM-DDTHH:MM:SSZ"}'

    response = requests.post('https://test4.oamportal.com/ServicesApi/rest/tag/', headers=headers, data=data)
    print(response)
    print(response.text)

#Request RFID tagID info
def requestRFIDtagID(token):
    print("requestRFIDtagID")
    headers = {
        'Authorization': 'Bearer ' + token,
    }

    response = requests.get('https://test4.oamportal.com/ServicesApi/rest/tag/[tag_id]', headers=headers)
    print(response)
    print(response.text)

#Increment transaction ID
#Transaction ID has format (8-4-4-4-12)
def incrementTransactionID(currentID):
    print("incrementing transaction ID")
    print(currentID)
    #Convert the format of the transactionID to an array of the format [8,4,4,4,12] where each integer is the length of that substring
    splitID = currentID.split("-")
    #Join all the array elements to one single string
    fullString = ''.join(map(str, splitID)) 
    #Convert the single string to an integer 
    integerID = int(fullString)
    #Increment the integer
    integerID+=1
    #Convert the integer back to a string
    incrementedStringID = str(integerID)
    #Fill the integer with zeroes until it is the correct length
    filledIncrementedStringID = incrementedStringID.zfill(8+4+4+4+12)
    #Add back the hyphens and add quotation marks to the beginning and end of the string (might be unnecessary)
    newTransactionID = "\"" + filledIncrementedStringID[:8] + "-" + filledIncrementedStringID[8:12] + "-" + filledIncrementedStringID[12:16] + "-" + filledIncrementedStringID[16:20] + "-" + filledIncrementedStringID[20:32] + "\""
    print(newTransactionID)
    #return the new transactionID which has been incremented by 1 and retains the same format
    return(newTransactionID)
