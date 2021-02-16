from scipy.optimize import linprog
import datetime

#TODO: Lösa hur man bestämmer EP(pris) till varje variabel Xi, Xi är varje 5 minuters current nivå, detta blir
#TODO: En array med alla current värden fram till den bestämda tiden
#TODO: Bestämma längd på arrayer och kwh utifrån angivna parametrar(Hur många Xi som behövs)
#TODO: Detta tar inte hänsyn till PV forecast änsålänge
V=400                   #Fast värde
priser = {              #läs in från mockdata

    13:86,
    14:79,
    15:80,
    16: 87,
    17: 86,
    18: 95,
    19: 87,
    20: 85,
    21: 78,
    22: 74,
    23: 72,
    0: 67,
    1: 65,
    2: 50,
    3: 45,
    4: 46,
    5: 45,
    6: 58,
    7: 68,
}
kvot = V*5/60000          #Fast värde
time_now = datetime.datetime.now()
print(time_now)
end_time = datetime.datetime(2021,2,13,8,0,0)##yyyy-mm.DD.HH.MM

print(end_time-time_now)
chargetime = end_time-time_now
time_minutes = chargetime.total_seconds()/60
print(time_minutes)
time_minutes -=  time_minutes % 5
intervall = time_minutes/5
print(intervall)
inter = int(intervall)
z = time_now + datetime.timedelta(minutes = 5)
print(z)



                            #Beräkna tid i minuter
                           #Golva tiden till multipel av 5
                         #(så många 5 minutare på tiden) --> Så många Xi variabler av current

obj = [kvot]*inter
print (obj)
i=0
while i<inter:
    y = int(time_now.strftime("%H"))
    time_now = time_now + datetime.timedelta(minutes = 5)
    obj[i] = obj[i]*priser[y]
    i += 1



#obj(0) = Ep[time_now+i*5minuter]      #Längd = antal 5 minuter på tillgänglig tid, Multipliceras med motsvarande pris
#      ─┬  ─┬
#       │   └┤ Coefficient for y    Vilket pris som tillhör tidsintervallet
#       └────┤ Coefficient for x


lhs_eq = [[kvot]*inter]  # Längd = antal 5 minuter på tillgänglig tid
print(lhs_eq)
rhs_eq = [20]       # Antal KwH vi behöver

bnd = [(0, 5)  # Bounds of x        Current, mellan 0 och currentlimit
      ]*inter  # Bounds of y
print(len(obj))
print(len(lhs_eq), len(lhs_eq[0]))
print(len(bnd), len(bnd[0]))
opt = linprog(c=obj,
              A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
            method="revised simplex")
print(opt.x)