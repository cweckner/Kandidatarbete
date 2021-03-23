import datetime


mon = 1
day = 1
hou = 0
tidspris = {

}
for j in range(3 * 24 + 1):
    tidspris[datetime.datetime(2021, mon, day, hou, 0, 0)] =  60
    hou = (hou + 1) % 24
    if hou == 0:
        day = day + 1
    if day == 30:
        mon = mon + 1

print(tidspris)