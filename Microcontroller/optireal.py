from scipy.optimize import linprog
import datetime
import matplotlib.pyplot as plt
import parameters

#def solarpower(intervall):
    #TODO: Returnera en array med storlek inter och Ampere värden som solpanelerna kan ge ut
    #Läs av från tiden nu och scanna framåt med 5 minuter varje gång, solen ges i kvartar så avrunda t närmsta kvart
    #Rebase ger en array med tider och en med KW,  KW = 400 * I, fråga Ali / David om detta
 #   solamp = []
 #   i = 0
 #   for j in range (intervall+1):
 #       solamp[j] = aisol [i]
 #       solamp[j+1] = aisol [i]
 #       solamp[j+2] = aisol [i]
 #       j = j + 3
 #       i = i + 1

  #  return solamp
def current(end_time,current_limit,capacity,battery_goal,battery_current):
    V=400                                               #Fast värde från laddstolpen
    kwh = (battery_goal-battery_current)*capacity/100   #Omvandling till kWh från batteriparametrar
    if kwh < 0:
        kwh = 0                                     #Buggkoll
    time_now = datetime.datetime.now()             #Tiden just nu
    priser = parameters.param(time_now,end_time)    #Anropa parametrar för att få pristabell
    kvot = V*5/60000                                #Fast värde, kwh/5 minuter= Kvot*I(Ampere)
    chargetime = end_time - time_now                #Laddningstid exakt
    time_minutes = chargetime.total_seconds()/60    #Laddningstid i minuter
    inter = int(time_minutes/5)                     #Omvandling till 5 minuters intervall
    inter = min(inter,288)                          #288 för 24 timmar

    if(inter == 0):
        inter = 1                                   #Förhindrar att koden kraschar när det är mindre än 5 min kvar

    obj = [kvot]*inter                              #Initialisera obj
    i=0                                             #loop-variabel
    while i<inter:                                  #Fyller obj med motsvarande pris för motsvarande tid
        tidsavrund = (time_now+datetime.timedelta(minutes = 30))
        #Beräknar hur många kwh vi har att använda
        # sol_el = getkwh(tid) 1645 - 15kw
        # kwhför5min = 32A * 4 kwh det blir
        # if sol_el >= kwhför5min           #Pseudocode för sol forecast
        #    obj[i] = 0
        #    sol_el - kwhför5min
        obj[i] = obj[i] * priser[datetime.datetime(tidsavrund.year, tidsavrund.month, tidsavrund.day, tidsavrund.hour)]
        time_now = time_now + datetime.timedelta(minutes=5)
        i += 1


    lhs_eq = [[kvot]*inter]                         #Beräkning av KWh

    rhs_eq = [kwh]                                  #Krav på hur många KWh vi behöver

    bnd = [(0, current_limit)]*inter                #Current, mellan 0 och currentlimit // Antingen 0, eller mellan 6 och MAX
   # bnd [0] = (10,current_limit)                    #Lägg in strömmen som kan fås ut från solpaneler här
    opt = linprog(c=obj,                            #Solver, minimimerar
    A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
    method="revised simplex")
    if opt.x[0] < 6 and opt.x[0]!=0:
        opt.x[0] = 6                                #Tillfällig silvertejpslösnings
    return opt.x

#tid = datetime.datetime(2021,4,8,15,19,0)
#plan = current(tid,32,63,100,20)                    #Värden för attt testa
#print(plan)
#for j in range(288):
 #   print(datetime.datetime.now()+datetime.timedelta(minutes=5*j),plan[j])  #Tabell tid/Chargecurrent
