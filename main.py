from Microcontroller import commands
id= "00000000-0000-0000-0000-000000000000"
id = commands.incrementTransactionID(id)
token = commands.createToken()
commands.requestSiteInfo(token)
commands.connectorStatus(token)
#commands.startCharger(token)
commands.consumedEnergy(token)
commands.changeActiveCurrent(token)
commands.stopCharger(token,id)
commands.setRFIDtagID(token)


'''
for length of array of optimised charging
    start charger
    when time gone = 5 min
        change active current
    "transactionId" : "00000000-0000-0000-0000-000000000000"
'''

