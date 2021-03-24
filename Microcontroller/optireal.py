from scipy.optimize import linprog
import datetime
#from Microcontroller import parameters
import parameters
def current(end_time,current_limit,capacity,battery_goal,battery_current,tid_nu):
    V=400
    kwh = (battery_goal-battery_current)*capacity/100   #Omvandling till kWh
    time_now = tid_nu #datetime.datetime.now()      #Tiden right now
    priser = parameters.param(time_now,end_time)    #Anropa parametrar för att få pristabell
    
#TODO: Lösa hur man bestämmer EP(pris) till varje variabel Xi, Xi är varje 5 minuters current nivå, detta blir
#TODO: En array med alla current värden fram till den bestämda tiden
    kvot = V*5/60000          #Fast värde       #typ kwh/5 minuter
    #end_time = datetime.datetime(2021,2,13,8,0,0)##yyyy-mm.DD.HH.MM
    chargetime = end_time - time_now        #Laddningstid exakt
    time_minutes = chargetime.total_seconds()/60    #Laddningstid i minuter
    time_minutes -=  time_minutes % 5           #Omvandla till intervall av 5 minuter, och sedan till int
    intervall = time_minutes/5                  #Drar även bort resten från mod division
    #print(end_time-time_now)
    #print("tids duration")
    #print(intervall)
    #print("5 minuters intervall")
    inter = int(intervall)
    inter = min(inter,288)      # 288 för 24 timmar
    if(inter == 0):
        inter = 1
    #print(inter)
    #print("inter avrundat t antal 5or")
    obj = [kvot]*inter          #Initialisera obj
    i=0
    while i<inter:              #Fyller obj med motsvarande pris för motsvarande tid
        z = int((time_now+datetime.timedelta(minutes = 0)).strftime("%H"))
        y = int((time_now+datetime.timedelta(minutes = 30)).strftime("%H"))
        if z == 23 and y == 0:
            obj[i] = obj[i] * priser[datetime.datetime(time_now.year, time_now.month, time_now.day+1, y)]
        else:
            obj[i] = obj[i]*priser[datetime.datetime(time_now.year,time_now.month,time_now.day,y)]
        time_now = time_now + datetime.timedelta(minutes=5)
        i += 1

    lhs_eq = [[kvot]*inter]     #Beräkning av KWh

    rhs_eq = [kwh]   #Krav på hur många KWh vi behöver

    bnd = [(0, current_limit)]*inter    # Current, mellan 0 och currentlimit // Antingen 0, eller mellan 6 och MAX
    opt = linprog(c=obj,        #Solver, minimize
    A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
    method="revised simplex")
    #print(sum(opt.x)*kvot)
    #print (opt.x)
    if opt.x[0] < 6 and opt.x[0]!=0:
        opt.x[0] = 6            #Tillfällig silvertejpslösnings
    return opt.x[0]

#tid = datetime.datetime(2021,3,27,6,45,0)
#print(current(tid,32,63,100,90))
