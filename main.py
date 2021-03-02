from Microcontroller import commands#, optireal
#from Display import main as disp
import datetime
import sched
import time
'''
transactionID= "00000000-0000-0000-0000-000000000000"
transactionID = commands.incrementTransactionID(transactionID)
connector = "1"
current = "10"
time = "2020-02-20 10:10:10"
intervalStart = datetime.datetime.now().strftime('%Y-%m-%d')
print(intervalStart)
intervalEnd = datetime.datetime.now().strftime('%Y-%m-%d')
timeSetRFIDtagID = commands.timeConverter(time, "setRFIDtagID")
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

token = commands.createToken()
tagID = "918273645"

commands.requestRFIDtagID(token,tagID)
'''

'''
for length of array of optimised charging
    start charger
    when time gone = 5 min
        change active current
    "transactionId" : "00000000-0000-0000-0000-000000000000"
'''
'%Y-%m-%d %H:%M:%S'
#commands.timeConverter("2020-02-26 14:47:20","consumedEnergy")

#Delay for 5 minutes
def delay():
    sched.scheduler(time.time(), time.sleep(300))



screen = disp.DemoApp().run()
transactionID= "00000000-0000-0000-0000-000000000000"
tagID = "918273645"

while(screen.start == 1):
    token = commands.createToken()
    currentTransactionID = commands.incrementTransactionID(transactionID)
    commands.startCharger(token,currentTransactionID,tagID)
    timeString = str(screen.datepicker) + str(screen.timepicker)
    endTimeCharging = datetime.datetime.strptime(timeString, '%Y-%m-%d %H:%M:%S')
    numberOfUpdates = commands.calculateNumberOfUpdates(endTimeCharging)



    chargingCurrent = optireal.current(endTimeCharging, screen.maxcurrenttf, screen.batterytf, screen.wantedtf, screen.currenttf)

