from scipy.optimize import linprog
#TODO: Lösa hur man bestämmer EP(pris) till varje variabel Xi, Xi är varje 5 minuters current nivå, detta blir
#TODO: En array med alla current värden fram till den bestämda tiden
#TODO: Bestämma längd på arrayer och kwh utifrån angivna parametrar(Hur många Xi som behövs)
#TODO: Detta tar inte hänsyn till PV forecast änsålänge
V=400                   #Fast värde
Ep1 = 100               #Läs in från mockdata
Ep2 = 20
kvot = V*5/60000          #Fast värde
current_time = 17.02
end_time = 8.00
chargetime = 14.58         #Beräkna tid i minuter
                           #Golva tiden till multipel av 5
ctime = 179 #(så många 5 minutare på tiden) --> Så många Xi variabler av current

obj = [Ep1*kvot, Ep2*kvot]       #Längd = antal 5 minuter på tillgänglig tid, Multipliceras med motsvarande pris
#      ─┬  ─┬
#       │   └┤ Coefficient for y    Vilket pris som tillhör tidsintervallet
#       └────┤ Coefficient for x


lhs_eq = [[kvot, kvot]]  # Längd = antal 5 minuter på tillgänglig tid
rhs_eq = [20]       # Antal KwH vi behöver

bnd = [(0, float("inf")),  # Bounds of x        Current, mellan 0 och currentlimit
      (0, float("inf"))]  # Bounds of y
opt = linprog(c=obj,
              A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
            method="revised simplex")
print(opt)