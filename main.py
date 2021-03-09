from Microcontroller import commands, optireal
from Display import main as disp
import datetime
import sched
import time

#Delay for 5 minutes
def delay():
    sched.scheduler(time.time(), time.sleep(300))

#First time starting the device
screen = disp.DemoApp().run()
transactionID= "00000000-0000-0000-0000-000000000000"
tagID = "918273645"

#Letting the device run forever it will run in this loop
while(True):
    if(screen.readytosend == True):
        #Initial inputs needed to continue
        token = commands.createToken()
        currentTransactionID = commands.incrementTransactionID(transactionID)

        timeString = str(screen.datepicker) + str(screen.timepicker)
        endTimeCharging = datetime.datetime.strptime(timeString, '%Y-%m-%d %H:%M:%S')
        numberOfUpdates = commands.calculateNumberOfUpdates(endTimeCharging)
        outlet = screen.outletcbx
        timeNow = datetime.datetime.strptime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        startDate = commands.timeConverter(timeNow, "consumedEnergy")
        endDate = commands.timeConverter(endTimeCharging, "consumedEnergy")

        stopTime = commands.timeConverter(endTimeCharging, "startCharger")
        commands.startCharger(token, currentTransactionID, tagID, stopTime)
        
        #This will be the loop that runs the whole charging process
        while(numberOfUpdates > 0):
            chargingCurrent = optireal.current(endTimeCharging, int(screen.maxcurrenttf), int(screen.batterytf), int(screen.wantedtf), int(screen.currenttf))
            print(chargingCurrent)
            outletStatus = commands.connectorStatus(token, outlet)
            if(outletStatus != "AVAILABLE"):
                commands.changeActiveCurrent(token, outlet, chargingCurrent)
                numberOfUpdates -= 1
                delay()
            else:
                #if the outlet is available -> car is not connected to the charger -> stop the charging loop
                break
        
        #All iterations done, stop the charger
        commands.consumedEnergy(token, tagID, startDate, endDate)
        commands.stopCharger(token, currentTransactionID)
        #Setting the ready variable to false so that the program will escape the current charging loop
        screen.readytosend = False
    #Restarting the screen to receive new input variables from the user
    disp.DemoApp().stop()
    disp.DemoApp().run()