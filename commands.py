import json
import datetime
import pytz
import requests

APIServer = 'https://test4.oamportal.com' 
databaseTag = "https://kandidat.ojensa.se/log/chargestorm/notify"
 
#Retrieve access token (authentication)
def createToken():
    #print("createToken")
    client_id = 'chalmers_test'
    client_secret = 'oWN3hmv9K6kYSGF96IP3pfWzrnk12Vo7'
    url = APIServer + "/oauth2/token"
    data = {
        'grant_type': 'client_credentials',
        'scope':'chargeportalservices'
    }

    response = requests.post(url, data=data, auth=(client_id,client_secret))
    #print(response.text)                           #debugging
    #print(response)                                 #debugging
    acc_response_json = response.json()             #Convert response to json object
    acc_token = acc_response_json["access_token"]   #Get the access token from the json object
    return(acc_token)                               #Return the access token so that it can be used later

#Start Charger
#Send the request to activate the connector on the charge station
#TODO:
#Add stoptime
def startCharger(token,transactionId,tagID, outletID):
    print("startCharger")
    if(outletID == 1):
        outlet = "d4ceb292-12ef-46b2-9724-0aeca7b62827"
    else:
        outlet = "fe294fba-d6ad-4616-8ab8-9999fe9bad58"
    tagIDSTR = "\""+tagID+"\""
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }
    url = APIServer + "/ServicesApi/rest/charger/uuid/start"
    data = '{"evseId":' +outlet+ ',"tagId":'+tagIDSTR+', "transactionId":' +transactionId+'}'
    response = requests.post(url, headers=headers, data=data)
    #print(data)
    print(response.text)
    
#Enable charger
def enableCharger(token,transactionId,tagID, outletID):
    print("enableCharger")
    if(outletID == 1):
        outlet = "d4ceb292-12ef-46b2-9724-0aeca7b62827"
    else:
        outlet = "fe294fba-d6ad-4616-8ab8-9999fe9bad58"
    tagIDSTR = "\""+tagID+"\""
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }
    url = APIServer + "/ServicesApi/rest/charger/uuid/start"
    data = '{"evseId":'+outlet+',"tagId":'+tagIDSTR+', "transactionId":' +transactionId+'}'
    response = requests.post(url, headers=headers, data=data)
    #print(data)
    print(response.text)

#Stop Charger
def stopCharger(token,transactionID, outletID):
    print("stopCharger")
    if(outletID == 1):
        outlet = "d4ceb292-12ef-46b2-9724-0aeca7b62827"
    else:
        outlet = "fe294fba-d6ad-4616-8ab8-9999fe9bad58"
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }
    url = APIServer + "/ServicesApi/rest/charger/uuid/stop"
    data = '{"evseId" : '+outlet+', "transactionId" :' +transactionID+'}'
    response = requests.post(url, headers=headers, data=data)
    #print(data)
    print(response)

#Notify Stop (request sent by charger)
#Server Response

#Change Active Current (amps)
#TODO:
#Add input from optimisation model
def changeActiveCurrent(token, connector, current):
    print("changeActiveCurrent")
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }
    url = APIServer + "/ServicesApi/rest/charger/changeactivecurrent"
    data = '{"current":' +current+ ', "chargeboxidentity": "000005354-1","connectorid":' +connector+ '}'
    response = requests.post(url, headers=headers, data=data)
    print(response)
    print(response.text)
    
#Consumed Energy (KWh) / duration
def consumedEnergy(token,tagID,intervalStart,intervalEnd):
    #print("consumedEnergy")
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }
    url = APIServer + "/ServicesApi/rest/tag/getSessionsByTag"
    data = '{"tagId" : '+tagID+', "intervalStart" : '+intervalStart+'," intervalEnd" : '+intervalEnd+'}'
    response = requests.post(url, headers=headers, data=data)
    return(response.text)
    #print(response)
    #print(response.text)

#Request Site Info
def requestSiteInfo(token):
    #print("requestSiteInfo")
    headers = {
    'Authorization': 'Bearer ' + token,
    'Content-Type': 'application/json',
    }
    url = APIServer + "/ServicesApi/rest/charger/siteinfo"
    data = '{"siteid" : "6d411116-91cc-4a61-9b83-b83380a04e69"}'
    response = requests.post(url, headers=headers, data=data)
    #print(response)
    #print(response.text)

#Get Connector Status
def connectorStatus(token, outletID):
    #print("connectorStatus")
    if(outletID == 1):
        outlet = "d4ceb292-12ef-46b2-9724-0aeca7b62827"
    else:
        outlet = "fe294fba-d6ad-4616-8ab8-9999fe9bad58"
    headers = {
        'Authorization': 'Bearer ' + token,
    }
    url = APIServer + "/ServicesApi/rest/charger/status/" + outlet
    response = requests.get(url, headers=headers)
    responseJSON = json.loads(response.text)
    status = responseJSON["status"]
    #print(response)
    #print(response.text)
    #print(status)
    return(status)

#Set RFID tagID
def setRFIDtagID(token, time):
    #print("setRFIDtagID")
    timeSTR = "\""+time+"\""
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json',
    }
    url = APIServer + "/ServicesApi/rest/tag/"
    data = '{"tagId":"918273645","companyId":170401,"validTo" :' +timeSTR+'}'
    response = requests.post(url, headers=headers, data=data)
    #print(response)
    #print(response.text)

#Request RFID tagID info
def requestRFIDtagID(token,tagID):
    #print("requestRFIDtagID")
    headers = {
        'Authorization': 'Bearer ' + token,
    }
    url = APIServer + "/ServicesApi/rest/tag/" + tagID
    response = requests.get(url, headers=headers)
    #print(response)
    #print(response.text)

#GET request to the server to retreive the current RFID tagID in use this charging session
'''
def getTagID(transactionID):
    url = databaseTag
    payload = json.dumps({
    "transactionID": transactionID
    })
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    responseJSON = json.loads(response.text)
    tagID = responseJSON["rfid"]
    #print(tagID)
    return tagID
'''

#Increment transaction ID
#Transaction ID has format (8-4-4-4-12)
def incrementTransactionID(currentID):
    #print("incrementing transaction ID")
    #print(currentID)
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
    newTransactionID = filledIncrementedStringID[:8] + "-" + filledIncrementedStringID[8:12] + "-" + filledIncrementedStringID[12:16] + "-" + filledIncrementedStringID[16:20] + "-" + filledIncrementedStringID[20:32]
    #print(newTransactionID)
    #return the new transactionID which has been incremented by 1 and retains the same format
    return(newTransactionID)

#Convert date to correct format depending on the command being sent
#The input timeToEdit should be a string
def timeConverter(timeToEdit,whichCommand):
    #print("timeConverter")
    #Input has format '%Y-%m-%d %H:%M:%S')
    timeSweden = pytz.timezone('Europe/Stockholm')
    utc = pytz.timezone('UTC')
    oldFormat = datetime.datetime.strptime(timeToEdit,'%Y-%m-%d %H:%M:%S')
    #print(oldFormat)
    oldFormatTimeZoneAware = timeSweden.localize(oldFormat)
    #print(oldFormatTimeZoneAware)
    if(whichCommand == "startCharger" or whichCommand == "setRFIDtagID"):
        #Format is "YYYY-MM-DDTHH:MM:SSZ"
        oldFormatUTC = oldFormatTimeZoneAware.astimezone(utc)
        newFormat = oldFormatUTC.strftime('%Y-%m-%dT%H:%M:%SZ')
        #print(newFormat)
        return(newFormat)
    elif(whichCommand == "consumedEnergy"):
        #Format is ""YYYY-MM-DD""
        newFormat = oldFormat.strftime('%Y-%m-%d')
        #print(newFormat)
        return(newFormat)
    else:
        return(oldFormat)

#Calculate the number of times to update the charging current
def calculateNumberOfUpdates(endTime):
    timeAtStart = datetime.datetime.now()
    #endTime = ("2021-03-02 20:00:00") #test time
    endTimeSeconds = datetime.datetime.strptime(endTime,'%Y-%m-%d %H:%M:%S')
    timeDelta = endTimeSeconds - timeAtStart
    chargetimeInSeconds = timeDelta.total_seconds()/60
    numberOfUpdates = (chargetimeInSeconds - (chargetimeInSeconds % 5))/5
    print(numberOfUpdates)
    return numberOfUpdates