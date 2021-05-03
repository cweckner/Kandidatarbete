from scipy.optimize import linprog
import datetime
import matplotlib.pyplot as plt
import parameters
import rebase_forecast

def current(end_time,current_limit,capacity,battery_goal,battery_current):
    V=230                                               #Fast värde från laddstolpen
    kwh = (battery_goal-battery_current)*capacity/100   #Omvandling till kWh från batteriparametrar
    if kwh < 0:
        kwh = 0                                     #Buggkoll
    time_now = datetime.datetime.now()             #Tiden just nu
    priser = parameters.param(time_now,end_time)    #Anropa parametrar för att få pristabell
    kvot = V*5/60000                                #Fast värde, kwh/5 minuter= Kvot*I(Ampere) (kVh)
    chargetime = end_time - time_now                #Laddningstid exakt
    time_minutes = chargetime.total_seconds()/60    #Laddningstid i minuter
    inter = int(time_minutes/5)                     #Omvandling till 5 minuters intervall
    inter = min(inter,288)                          #288 för 24 timmar

    if(inter == 0):
        inter = 1                              #Förhindrar att koden kraschar när det är mindre än 5 min kvar

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
    time = datetime.datetime.now().strftime("%H:%M")
    solcells_data = rebase_forecast.get_solar_forecast(time)  #Error hur anropar jag denna
    load_data = rebase_forecast.get_load_forecast(time)
    z = 0           #Loop-parametrar
    y = 0
    kw_to_amp = 1000/230
    for j in range(0,inter):
        #print((solcells_data[z] - load_data[y])*kw_to_amp)
        if j%3 == 0 and j != 0:         #14:55 z:14:45, y:14:00
            z = z + 1
        if z%4 == 0 and z != 0 and j%3 == 0 and j != 0:
            y = y + 1
        if int((solcells_data[z]-load_data[y])*kw_to_amp) > current_limit:
            bnd [j] = (current_limit,current_limit)
        elif int((solcells_data[z]-load_data[y])*kw_to_amp) < 3:
            bnd[j] = (0, current_limit)
        elif int((solcells_data[z]-load_data[y]*kw_to_amp)) < 6 and int((solcells_data[z]-load_data[y])*kw_to_amp) > 3:
            bnd [j] = (6,current_limit)                        #Lägg in strömmen som kan fås ut från solpaneler här
        else:
            bnd[j] = (int((solcells_data[z]-load_data[y])*kw_to_amp), current_limit)

            #bnd [j+1] = (solcellsdata[j],current_limit)                    #Lägg in strömmen som kan fås ut från solpaneler här
    #bnd [j+2] = (solcellsdata[j],current_limit)                    #Lägg in strömmen som kan fås ut från solpaneler här
                  #Kolla om det är likström eller växelström
    print(bnd)

    opt = linprog(c=obj,                            #Solver, minimimerar
    A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
    method="revised simplex")
    if opt.x[0] <= 3:
        opt.x[0] = 0                                #Tillfällig silvertejpslösnings
    if opt.x[0] <6 and opt.x[0]>3:
        opt.x[0] = 6
    return opt.x

#tid = datetime.datetime(2021,5,1,17,18,0)
#plan = current(tid,16,63,100,20)                    #Värden för attt testa
#print(plan)
#for j in range(288):
 #   print(datetime.datetime.now()+datetime.timedelta(minutes=5*j),plan[j])  #Tabell tid/Chargecurrent
