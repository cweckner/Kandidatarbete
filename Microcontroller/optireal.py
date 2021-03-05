from scipy.optimize import linprog
import datetime
from Microcontroller import parameters
def current(end_time,current_limit,capacity,battery_goal,battery_current):
    V=400
    kwh = (battery_goal-battery_current)*capacity/100
    time_now = datetime.datetime.now()
    priser = parameters.param(time_now,end_time)

#TODO: Lösa hur man bestämmer EP(pris) till varje variabel Xi, Xi är varje 5 minuters current nivå, detta blir
#TODO: En array med alla current värden fram till den bestämda tiden
    kvot = V*5/60000          #Fast värde
    #end_time = datetime.datetime(2021,2,13,8,0,0)##yyyy-mm.DD.HH.MM
    chargetime = end_time - time_now
    time_minutes = chargetime.total_seconds()/60
    time_minutes -=  time_minutes % 5           #Omvandla till intervall av 5 minuter, och sedan till int
    intervall = time_minutes/5                  #Drar även bort resten från mod division
    print(end_time-time_now)
    print(intervall)
    inter = int(intervall)
    inter = min(inter,144)
    print(inter)
    obj = [kvot]*inter          #Initialisera obj
    i=0
    while i<inter:              #Fyller obj med motsvarande pris för motsvarande tid
        y = int((time_now+datetime.timedelta(minutes = 30)).strftime("%H"))
        time_now = time_now + datetime.timedelta(minutes = 5)
        obj[i] = obj[i]*priser[y]
        i += 1

    lhs_eq = [[kvot]*inter]     #Beräkning av KWh

    rhs_eq = [kwh]   #Krav på hur många KWh vi behöver

    bnd = [(0, current_limit)]*inter    # Current, mellan 0 och currentlimit //
    opt = linprog(c=obj,        #Solver, minimize
    A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
    method="revised simplex")
    return opt.x[1]

end_time = datetime.datetime(2021,3,3,8,0,0)

print(current(end_time,32,100,80,20))
