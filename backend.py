import commands, optireal
import datetime
import sched
import time


class backend:

    transactionID0 = "00000000-0000-0000-0000-000000000000" #the transactionID will be handled by the front end to ease parallellism
    tagID = "918273645" #default id used for testing

    #readyVariable = True/False
    #carChargeAtStart = number in percent
    #carWantedCharge = number in percent
    #carBatteryCapacity = integer
    #carMaxCurrentInput = integer
    #departureTime = format as datetime.datetime.strptime(inputTime, '%Y-%m-%d %H:%M:%S')
    #transactionID = string "00000000-0000-0000-0000-000000000000"
    def chargingLoop(self, readyVariable, carChargeLevelNow, carWantedCharge, carBatteryCapacity, carMaxCurrentInput, departureTime, outlet, transactionID):
        if(readyVariable):
            #initial variables
            print(str(transactionID))
            tagID = self.tagID
            token = commands.createToken()
            numberOfUpdates = commands.calculateNumberOfUpdates(departureTime)
            otherOutlet = 3

            #set starting times, nextTime is set to equal currentTime to allow the program to start its
            #first loop and is then calculated inside the loop
            currentTime = datetime.datetime.now()
            nextTime = currentTime
            
            #comparingTime are used to stop the charger if it has gone past the set departure time
            #even if the car didn't reach the wanted final charge level
            comparingTimeNow = datetime.datetime.timestamp(currentTime)
            comparingTimeDeparture = datetime.datetime.timestamp(datetime.datetime.strptime(departureTime,'%Y-%m-%d %H:%M:%S'))
            
            #Charger specific voltage
            voltage = 400 

            #time format conversion for the consumedEnergy command to see how much energy it took to charge the car
            timeForStartDate = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
            startDate = commands.timeConverter(timeForStartDate, "consumedEnergy")
            endDate = commands.timeConverter(departureTime, "consumedEnergy")

            #time format conversion for the startCharger command so that it knows when its expected to stop
            stopTime = commands.timeConverter(departureTime, "startCharger")

            #time format for the optimimisation model
            timeTuple = time.strptime(departureTime, '%Y-%m-%d %H:%M:%S')
            timeTupleFull = (timeTuple.tm_year, timeTuple.tm_mon, timeTuple.tm_mday, timeTuple.tm_hour, timeTuple.tm_min)
            optTime = datetime.datetime(*timeTupleFull[0:4])

            #starting the charger
            commands.startCharger(token, transactionID, tagID, outlet)
            #tagID = commands.getTagID(transactionID)
            commands.changeActiveCurrent(token, str(outlet), str(0))

            #the charging loop
            while(numberOfUpdates > 0):
                if(int(carChargeLevelNow+0.5) >= carWantedCharge or comparingTimeNow >= comparingTimeDeparture):
                    commands.changeActiveCurrent(token, str(outlet), "0")
                    break
                #print("entered loop")
                #print("number of updates" + " " + str(numberOfUpdates))
                #check if a car is connected to the outlet we want to use
                outletStatus = commands.connectorStatus(token, outlet)
                
                #update currentTime to the time right now, FINAL PRODUCT
                #currentTime = datetime.datetime.now()

                #add 5 minutes to wait before updating the charging current, FINAL PRODUCT
                #nextTime = currentTime + datetime.timedelta(minutes = 5)

                #update what time it is, TESTING
                currentTime += datetime.timedelta(minutes = 5)

                #TESTING
                nextTime = currentTime

                comparingTimeNow = datetime.datetime.timestamp(currentTime)
                        
                #Switch the if cases depending on if you are testing or not
                #if(outletStatus != "AVAILABLE" and currentTime >= nextTime):
                print(currentTime)
                print(nextTime)
                if(currentTime >= nextTime):
                    #receiving the optimised charging current from the optimisation model
                    chargingCurrent = optireal.current(optTime, int(carMaxCurrentInput), int(carBatteryCapacity), int(carWantedCharge), int(carChargeLevelNow+0.5))
                    print(chargingCurrent)
                    #send the chargingCurrent to the charger to change the current
                    commands.changeActiveCurrent(token, str(outlet), str(chargingCurrent[0]))

                    #calculations to get the car's current percentage of battery charge
                    #how much kwh that represent 1 %
                    kwhAsPercent = carBatteryCapacity/100

                    #how much current we got from the charger
                    currentStatus = (voltage*5/60000)*chargingCurrent[0]
                    carChargeLevelNow += currentStatus/kwhAsPercent
                    print(str(int(carChargeLevelNow+0.5)) + "%")
                    #nextTime = currentTime + datetime.timedelta(minutes = 5)
                    numberOfUpdates -= 1
                    print(str(chargingCurrent[0]))
                    print(str(outlet))
                    print(str(numberOfUpdates))
                    #Log data
                    chargeLog = commands.consumedEnergy(token, tagID, startDate, endDate)
                    f = open("charginglog.txt", "a")
                    f.write(str(currentTime) + "\n")
                    f.write(str(chargingCurrent[0]) + "\n")
                    f.write(chargeLog + "\n")
                    f.close()

                    
            #All iterations done, or the car is not connected and the other outlet is not in use -> stop the charger
            #if(outlet == 1):
            #    otherOutlet = 2
            #else:
            #    otherOutlet = 1
            #otherOutletStatus = commands.connectorStatus(token, otherOutlet)
            commands.consumedEnergy(token, tagID, startDate, endDate)
            #if(otherOutlet == "AVAILABLE"):
            commands.stopCharger(token, transactionID, outlet)


#backendTest = backend()
#backendTest.chargingLoop( True, 20, 26, 100, 16, "2021-03-29 20:00:00", 1, backendTest.transactionID0)
