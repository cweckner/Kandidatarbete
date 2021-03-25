from scipy.optimize import linprog
import datetime
import matplotlib.pyplot as plt
import parameters

def current(end_time,current_limit,capacity,battery_goal,battery_current):
    V=400                                               #Fast värde från laddstolpen
    kwh = (battery_goal-battery_current)*capacity/100   #Omvandling till kWh från batteriparametrar
    if kwh < 0:
        kwh = 0                                     #Buggkoll
    time_now = datetime.datetime.now()              #Tiden just nu
    priser = parameters.param(time_now,end_time)    #Anropa parametrar för att få pristabell
    kvot = V*5/60000                                #Fast värde, kwh/5 minuter= Kvot*I(Ampere)
    chargetime = end_time - time_now                #Laddningstid exakt
    time_minutes = chargetime.total_seconds()/60    #Laddningstid i minuter
    inter = int(time_minutes/5)                     #Omvandling till 5 minuters intervall
    inter = min(inter,288)                          #288 för 24 timmar

    if(inter == 0):
        inter = 1                                   #minns ej varför jag gjorde detta men vågar inte ta bort den

    obj = [kvot]*inter                              #Initialisera obj
    i=0                                             #loop-variabel
    while i<inter:                                  #Fyller obj med motsvarande pris för motsvarande tid
        tidsavrund = (time_now+datetime.timedelta(minutes = 30))
        obj[i] = obj[i] * priser[datetime.datetime(tidsavrund.year, tidsavrund.month, tidsavrund.day, tidsavrund.hour)]
        time_now = time_now + datetime.timedelta(minutes=5)
        i += 1


    lhs_eq = [[kvot]*inter]                         #Beräkning av KWh

    rhs_eq = [kwh]                                  #Krav på hur många KWh vi behöver

    bnd = [(0, current_limit)]*inter                #Current, mellan 0 och currentlimit // Antingen 0, eller mellan 6 och MAX
    opt = linprog(c=obj,                            #Solver, minimimerar
    A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
    method="revised simplex")
    if opt.x[0] < 6 and opt.x[0]!=0:
        opt.x[0] = 6                                #Tillfällig silvertejpslösnings
    return opt.x

tid = datetime.datetime(2021,3,29,0,0,0)
plan = current(tid,32,63,100,20)                    #Värden för attt testa
xlables = []
for j in range(288):
    print(datetime.datetime.now()+datetime.timedelta(minutes=5*j),plan[j])  #Tabell tid/Chargecurrent
