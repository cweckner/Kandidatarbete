from commands import *


token = createToken()
requestSiteInfo(token)
connectorStatus(token)
notifyStart(token,startCharger(token))
consumedEnergy(token)
changeActiveCurrent(token)
notifyStop(token,stopCharger(token) )
setRFIDtagID(token)
#requestRFIDtagID(token) status code 500
