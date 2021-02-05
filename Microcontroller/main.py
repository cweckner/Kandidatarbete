from commands import *


token = createToken()
requestSiteInfo(token)
startCharger(token)
notifyStart(token)
consumedEnergy(token)
changeActiveCurrent(token)
stopCharger(token)
notifyStop(token)

