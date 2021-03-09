import commands, optireal
import datetime
import sched
import time


class backend:

    transactionID0 = "00000000-0000-0000-0000-000000000000"
    tagID = "918273645"

    #Delay for 5 minutes
    def delay():
        sched.scheduler(time.time(), time.sleep(1))

    #readyVariable = True/False
    #carChargeAtStart = number in percent
    #carWantedCharge = number in percent
    #carBatteryCapacity = integer
    #carMaxCurrentInput = integer
    #departureTime = format as datetime.datetime.strptime(inputTime, '%Y-%m-%d %H:%M:%S')
    #transactionID = string "00000000-0000-0000-0000-000000000000"
    #tagID = string of integers 
    def chargingLoop(self, readyVariable, carChargeLevelNow, carWantedCharge, carBatteryCapacity, carMaxCurrentInput, departureTime, outlet, transactionID, tagID):
        if(readyVariable):
            #initial variables
            token = commands.createToken()
            currentTransactionID = commands.incrementTransactionID(transactionID)
            numberOfUpdates = commands.calculateNumberOfUpdates(departureTime)
            chargingOutlet = outlet
            otherOutlet = 3
            currentTime = datetime.datetime.now()
            nextTime = datetime.datetime.now()
            comparingTimeNow = datetime.datetime.timestamp(currentTime)
            comparingTimeDeparture = datetime.datetime.timestamp(datetime.datetime.strptime(departureTime,'%Y-%m-%d %H:%M:%S'))
            voltage = 400 #Charger specific voltage

            #time format conversion for the consumedEnergy command to see how much energy it took to charge the car
            timeForStartDate = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
            startDate = commands.timeConverter(timeForStartDate, "consumedEnergy")
            endDate = commands.timeConverter(departureTime, "consumedEnergy")

            #time format conversion for the startCharger command so that it knows when its expected to stop
            stopTime = commands.timeConverter(departureTime, "startCharger")

            #time format for optimimisation model
            timeTuple = time.strptime(departureTime, '%Y-%m-%d %H:%M:%S')
            timeTupleFull = (timeTuple.tm_year, timeTuple.tm_mon, timeTuple.tm_mday, timeTuple.tm_hour, timeTuple.tm_min)
            optTime = datetime.datetime(*timeTupleFull[0:4])
            #print(optTime)



            #starting the charger
            commands.startCharger(token, currentTransactionID, tagID, stopTime)

            #the charging loop
            while(numberOfUpdates > 0):
                if(carChargeLevelNow >= carWantedCharge or comparingTimeNow >= comparingTimeDeparture):
                    break
                print("entered loop")
                print("number of updates" + " " + str(numberOfUpdates))
                #check if a car is connected to the outlet we want to use
                outletStatus = commands.connectorStatus(token, chargingOutlet)
                #update currentTime to the time right now
                currentTime = datetime.datetime.now()
                #if(outletStatus != "AVAILABLE" and currentTime >= nextTime):
                if(currentTime >= nextTime):
                #if(True):
                    #receiving the optimised charging current from the optimisation model
                    chargingCurrent = optireal.current(optTime, int(carMaxCurrentInput), int(carBatteryCapacity), int(carWantedCharge), int(carChargeLevelNow+0.5), currentTime)

                    #calculations to get the car's current percentage of battery charge
                    #how much kwh that represent 1 %
                    kwhAsPercent = carBatteryCapacity/100

                    #how much current we got from the charger
                    currentStatus = (voltage*5/60000)*chargingCurrent[0]
                    carChargeLevelNow += currentStatus/kwhAsPercent
                    print(str(int(carChargeLevelNow+0.5)) + "%")

                    #update what time it is, only for simulation
                    #currentTime += datetime.timedelta(minutes = 5)
                    #print(currentTime)

                    #instead of using delay function check if 5 minutes have passed
                    nextTime = currentTime + datetime.timedelta(minutes = 5)

                    numberOfUpdates -= 1
                    #self.delay()
                #if the outlet is available -> no car is connected to the outlet -> stop the charging
                #elif(outletStatus == "AVAILABLE"):
                    #break
                    
            #All iterations done, or the car is not connected and the other outlet is not in use -> stop the charger
            if(outlet == 1):
                otherOutlet = 2
            else:
                otherOutlet = 1
            otherOutletStatus = commands.connectorStatus(token, otherOutlet)
            commands.consumedEnergy(token, tagID, startDate, endDate)
            if(otherOutlet == "AVAILABLE"):
                commands.stopCharger(token, currentTransactionID)


#backendTest = backend()
#backend.chargingLoop(backend, True, 20, 40, 100, 16, "2021-03-09 20:00:00", 1, backend.transactionID0, backend.tagID)