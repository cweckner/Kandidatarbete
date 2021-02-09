from Microcontroller import commands

token = commands.createToken()
commands.requestSiteInfo(token)
commands.connectorStatus(token)
commands.startCharger(token)
commands.notifyStart(token)
commands.consumedEnergy(token)
commands.changeActiveCurrent(token)
commands.stopCharger(token)
commands.notifyStop(token)
commands.setRFIDtagID(token)