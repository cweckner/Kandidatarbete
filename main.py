from Microcontroller import commands, optireal
#from Display import main as disp
import datetime

transactionID= "00000000-0000-0000-0000-000000000000"
transactionID = commands.incrementTransactionID(transactionID)
connector = "1"
current = "10"
time = "2020-02-20 10:10:10"
tagID = "918273645"
intervalStart = datetime.datetime.now().strftime('%Y-%m-%d')
print(intervalStart)
intervalEnd = datetime.datetime.now().strftime('%Y-%m-%d')
timeSetRFIDtagID = commands.timeConverter(time, "setRFIDtagID")
token = commands.createToken()
commands.requestSiteInfo(token)
commands.connectorStatus(token)
timeStop = commands.timeConverter(time,"startCharger")
commands.startCharger(token,transactionID,tagID,timeStop)
commands.consumedEnergy(token,tagID,intervalStart,intervalEnd)
commands.changeActiveCurrent(token,connector,current)
commands.stopCharger(token,transactionID)
commands.setRFIDtagID(token,timeSetRFIDtagID)
#optireal.current()
commands.stopCharger(token,transactionID)
#commands.requestRFIDtagID(token,tagID)


'''
for length of array of optimised charging
    start charger
    when time gone = 5 min
        change active current
    "transactionId" : "00000000-0000-0000-0000-000000000000"
'''
'%Y-%m-%d %H:%M:%S'
commands.timeConverter("2020-02-26 14:47:20","consumedEnergy")


#start screen
#while screen object start = 1
    #create token
    #screen object time

