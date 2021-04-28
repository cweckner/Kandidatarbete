import commands
import datetime
import time


token = commands.createToken()

transactID = str("00000000-0000-0000-0000-000000000500")
print(commands.connectorStatus(token, 1))
time.sleep(10)
print(1)
commands.enableCharger(token, transactID, "123456", 1)
print(commands.connectorStatus(token, 1))
time.sleep(10)
print(2)
commands.startCharger(token, transactID,"123456",1)
print(commands.connectorStatus(token, 1))

time.sleep(10)
print(3)
commands.changeActiveCurrent(token, "1", "6")
print(commands.connectorStatus(token, 1))

time.sleep(10)

chargeLog = commands.consumedEnergy(token, "123456", "2021-04-28", "2021-04-28")

timeprint = datetime.datetime.now()

f = open("chargingLogTest.txt", "a")
f.write(str(timeprint))
f.write(chargeLog + "\n")
f.close()

time.sleep(300)

chargeLog2 = commands.consumedEnergy(token, "12345", "2021-04-28", "2021-04-28")

timeprint2 = datetime.datetime.now()

f = open("chargingLogTest.txt", "a")
f.write(str(timeprint2))
f.write(chargeLog2 + "\n")
f.close()
commands.stopCharger(token, transactID, 1)


time.sleep(10)
print(commands.connectorStatus(token, 1))

chargeLog3 = commands.consumedEnergy(
    token, "12345", "2021-04-28", "2021-04-28")

timeprint3 = datetime.datetime.now()

f = open("chargingLogTest.txt", "a")
f.write(str(timeprint3))
f.write(chargeLog3 + "\n")
f.close()
