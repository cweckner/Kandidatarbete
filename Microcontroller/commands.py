import json
import datetime

'''
Statuses
UNKNOWN - (just before CHARGING)
CHARGING - after starting
SUSPENDEDEV - just before CHARGING or after setting current to zero
PREPARING - after plugging in
AVAILABLE - nothing plugged in
FINISHING - after trying to send NotifyStart?
UNAVAILIBLE
REJECTED_BY_CHARGEPOINT
MALFORMED_URL - (misleading) has happened due to expecting a UUID in the request
'''

'''
Essential Information
CompanyID: 170401
Living Lab EV charger siteID: 6d411116-91cc-4a61-9b83-b83380a04e69
chargeboxid/chargeboxidentity: 000005354-1
chargeboxuuid: ef8595c4-fb55-42b6-8dfa-26e3dd5d2146
evsID/outletuuid:
    connectorID 1: d4ceb292-12ef-46b2-9724-0aeca7b62827
    connectorID 2: fe294fba-d6ad-4616-8ab8-9999fe9bad58
TransactionID format (8-4-4-4-12):
    00000000-0000-0000-0000-000000000000
Timestamp formats (inconsistent!)
    stoptime (remoteStart request): YYYY-MM-DDTHH:MM:SSZ
    validTo (set tagID request/get tagID info response): YYYY-MM-DDTHH:MM:SSZ
    NotifyStart/NotifyStop requests: YYYY-MM-DDTHH:MM:SS.000+01:00
    intervalStart/intervalEnd (getSessionsByTag request): YYYY-MM-DD
    startDate/stopDate (getSessionsByTag response): YYYY-MM-DD HH:MM:SS
'''

#Retrieve access token (authentication)
'''
Request /oauth2/token:
curl https://test4.oamportal.com/oauth2/token -d 'grant_type=client_credentials' 
-d 'scope=chargeportalservices' --user '[client_id]:[client_secret]'

Response: access token:
{"access_token":"[access_token]","expires_in":3599,"scope":
"chargeportalservices","token_type":"bearer"}
'''
#Start Charger
'''
Request: remoteStart (connector 1):
curl https://test4.oamportal.com/ServicesApi/rest/charger/uuid/start
-H 'Authorization: Bearer [access_token]' -H 'Content-Type: application/json'
-d '{"evseId":"d4ceb292-12ef-46b2-9724-0aeca7b62827","tagId":"[tag_id]",
"transactionId":"00000000-0000-0000-0000-000000000000",
"stoptime":"YYYY-MM-DDTHH:MM:SSZ"}'

Response (connector 1):
{"evseId":"d4ceb292-12ef-46b2-9724-0aeca7b62827","success":true,
"errorCode":"NO_ERROR","transactionId":[transaction_id]}
'''
#Notify Start (request sent by charger)
'''
Request: NotifyStart (connector 1):
{"messageType":"transactionStart","evseId":"d4ceb292-12ef-46b2-9724-0aeca7b62827",
"tagId":"[tag_id]","timeStamp":"YYYY-MM-DDTHH:MM:SS.000+01:00",
"sessionId":"[session_id]","transactionId":"00000000-0000-0000-0000-000000000000"}

Response:
curl https://test4.oamportal.com/ServicesApi/rest/charger/uuid/start -H
'Authorization: Bearer [access_token]' -H 'Content-Type: application/json'
-d '{"accepted" : true,"errorCode" : "NO_ERROR"}'
'''
#Stop Charger
'''
Request: remoteStop (connector 1):
curl https://test4.oamportal.com/ServicesApi/rest/charger/uuid/stop -H
'Authorization: Bearer [access_token]' -H 'Content-Type: application/json'
-d '{"evseId" : "d4ceb292-12ef-46b2-9724-0aeca7b62827",
"transactionId" : "00000000-0000-0000-0000-000000000000"}'

Response (connector 1):
{"evseId":"d4ceb292-12ef-46b2-9724-0aeca7b62827","success":true,"errorCode":"NO_ERROR",
"transactionId":"00000000-0000-0000-0000-000000000000"}
'''
#Notify Stop (request sent by charger)
'''
Request: NotifyStop (connector 1):
{"messageType":"transactionStop","evseId":"d4ceb292-12ef-46b2-9724-0aeca7b62827",
"kWh":"[kWh]","timeStamp":"YYYY-MM-DDTHH:MM:SS.000+01:00",
"sessionId":"[session_id]","transactionId":"00000000-0000-0000-0000-000000000000"}

Response:
curl https://test4.oamportal.com/ServicesApi/rest/charger/uuid/stop -H
'Authorization: Bearer [access_token]' -H 'Content-Type: application/json'
-d '{"accepted" : true,"errorCode" : "NO_ERROR"}'
'''
#Change Active Current (amps)
'''
Request: changeactivecurrent:
curl https://test4.oamportal.com/ServicesApi/rest/charger/changeactivecurrent
-H 'Authorization: Bearer [access_token]' -H 'Content-Type: application/json'
-d '{"current": "[current]", "chargeboxidentity": "000005354-1","connectorid": "1"}'

Response: example when no car plugged in:
{"status":"rejected","errorcode":"Not allowed: chargebox has no active charging session"}
'''
#Consumed Energy (KWh) / duration
'''
Request: getSessionsByTag
curl https://test4.oamportal.com/ServicesApi/rest/tag/getSessionsByTag
-H 'Authorization: Bearer [access_token]' -H 'Content-Type: application/json'
-d '{"tagId" : "[tag_id]", "intervalStart" : "YYYY-MM-DD"," intervalEnd" : "YYYY-MM-DD"}'

Response: 
{"sessions": [
{"sessionId": "[session_id]","consumedEnergyInKWh": "0.0",
"durationInSeconds": "10", "startDate": "YYYY-MM-DD HH:MM:SS",
"stopDate": "YYYY-MM-DD HH:MM:SS","chargeBoxIdentity": "000005354-1","connectorId": "1"},
{"sessionId": "[session_id]","consumedEnergyInKWh": "0.0",
"durationInSeconds": "8988","startDate": "YYYY-MM-DD HH:MM:SS",
"stopDate": "YYYY-MM-DD HH:MM:SS","chargeBoxIdentity": "000005354-1","connectorId": "1"}
],
"count": 2}
'''
#Request Site Info
'''
Request: charger/siteinfo:
curl https://test4.oamportal.com/ServicesApi/rest/charger/siteinfo
-H 'Authorization: Bearer [access_token]'
-H 'Content-Type: application/json' -d '{"siteid" : "6d411116-91cc-4a61-9b83-b83380a04e69"}'

Response: 
{"sitename":"Chalmers e2","stations":
[{"chargeboxid":"000005354-1","latitude":"0.0","longitude":"0.0",
"chargeboxname":"Chargestorm Connected",
"chargeboxuuid":"ef8595c4-fb55-42b6-8dfa-26e3dd5d2146",
"outlets":[{"connectorid":1,"outletuuid":"d4ceb292-12ef-46b2-9724-0aeca7b62827",
"state":"AVAILABLE","mode":"RFID","connectortype":"TYPE2"},
{"connectorid":2,"outletuuid":"fe294fba-d6ad-4616-8ab8-9999fe9bad58",
"state":"AVAILABLE","mode":"RFID","connectortype":"TYPE2"}]}]}
'''
#Get Connector Status
'''
Request: charger/status/[EVSID] (connector 1):
curl https://test4.oamportal.com/ServicesApi/rest/charger/status/d4ceb292-12ef-46b2-9724-0aeca7b62827 
-H 'Authorization: Bearer [access_token]'

Response (connector 1):
{"evseId":"d4ceb292-12ef-46b2-9724-0aeca7b62827","status":"AVAILABLE","busyTimer":0,"alarm":0}
'''
#Set RFID tagID
'''
Request: 
curl -4 https://test4.oamportal.com/ServicesApi/rest/tag/
-H 'Authorization: Bearer [access_token]' -H 'Content-Type: application/json'
-d '{"tagId":"918273645","companyId":170401,"validTo" : "YYYY-MM-DDTHH:MM:SSZ"}'

Response
{"companyId":"170401","tagId":"[tag_id]","status":"SUCCESS"}
'''
#Request RFID tagID info
'''
Request: 
curl https://test4.oamportal.com/ServicesApi/rest/tag/[tag_id]
-H 'Authorization: Bearer [access_token]'

Response:
{"tagId":"[tag_id]","company":[{"companyId":170401,"validTo":"YYYY-MM-DDTHH:MM:SSZ"}]}
'''
