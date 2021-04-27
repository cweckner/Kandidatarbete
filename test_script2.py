import commands
import time

transactID = str("00000000-0000-1110-0000-000000000000")
token = commands.createToken()
commands.connectorStatus(token, 1)

commands.enableCharger(token, transactID, "1234", 1)
commands.startCharger(token, transactID,"1234",1)

commands.changeActiveCurrent(token, "1", "8")

chargeLog = commands.consumedEnergy(token, "1234", "2021-04-27", "2021-04-27")

f = open("chargingLogTest.txt", "a")
f.write(chargeLog + "\n")
f.close()

time.sleep(10)

chargeLog2 = commands.consumedEnergy(token, "1234", "2021-04-27", "2021-04-27")

f = open("chargingLogTest.txt", "a")
f.write(chargeLog2 + "\n")
f.close()
