from Microcontroller import commands, optireal

token = commands.createToken()
commands.requestSiteInfo(token)
commands.connectorStatus(token)
commands.startCharger(token)
commands.consumedEnergy(token)
commands.changeActiveCurrent(token)
commands.stopCharger(token)
commands.setRFIDtagID(token)
optireal.current()