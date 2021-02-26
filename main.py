from Microcontroller import commands

token = commands.createToken()
commands.requestSiteInfo(token)
commands.connectorStatus(token)
#commands.startCharger(token)
commands.consumedEnergy(token)
commands.changeActiveCurrent(token)
commands.stopCharger(token)
commands.setRFIDtagID(token)


'''
for length of array of optimised charging
    start charger
    when time gone = 5 min
        change active current
    "transactionId" : "00000000-0000-0000-0000-000000000000"
'''
id= "00000000-0000-0000-0000-000000000000"
id = commands.incrementTransactionID(id)
