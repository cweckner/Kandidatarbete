from Microcontroller import commands
transactionID= "00000000-0000-0000-0000-000000000000"
transactionID = commands.incrementTransactionID(transactionID)
token = commands.createToken()
commands.requestSiteInfo(token)
commands.connectorStatus(token)
commands.startCharger(token,transactionID)
commands.consumedEnergy(token)
commands.changeActiveCurrent(token)
commands.stopCharger(token,transactionID)
commands.setRFIDtagID(token)


'''
for length of array of optimised charging
    start charger
    when time gone = 5 min
        change active current
    "transactionId" : "00000000-0000-0000-0000-000000000000"
'''

