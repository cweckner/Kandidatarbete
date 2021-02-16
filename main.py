from Microcontroller import commands

token = commands.createToken()
commands.requestSiteInfo(token)
commands.connectorStatus(token)
commands.startCharger(token)
commands.consumedEnergy(token)
commands.changeActiveCurrent(token)
commands.stopCharger(token)
commands.setRFIDtagID(token)