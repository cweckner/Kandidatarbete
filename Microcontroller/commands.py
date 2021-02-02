import json

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

#Retrieve access token (authentication)

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

#