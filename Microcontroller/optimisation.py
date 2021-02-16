#Detta e bah test änsålänge

from scipy.optimize import linprog

obj = [-1, -2]
#      ─┬  ─┬
#       │   └┤ Coefficient for y
#       └────┤ Coefficient for x

lhs_ineq = [[ 2,  1],  # Red constraint left side
             [-4,  5],  # Blue constraint left side
             [ 1, -2]]  # Yellow constraint left side

rhs_ineq = [20,  # Red constraint right side
            10,  # Blue constraint right side
            2]  # Yellow constraint right side

lhs_eq = [[-1, 5]]  # Green constraint left side
rhs_eq = [15]       # Green constraint right side

bnd = [(0, float("inf")),  # Bounds of x
      (0, float("inf"))]  # Bounds of y
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
            method="revised simplex")
print(opt)

#Kopplas in 17, Ska åka 08, ladda från 20%-80%
ep0 = [94,109,88,73,64,58,53,46,46,46,46,46,48,58,83]
h0 = [17.05,17.10,17.15,17.20,] #Dictionary 5 min intervall varje tid har ett värde på current

pris = 1;
c = [ #12 Värden för varje timme, v

    [1,2,3,4,5,6,7,8,9,10,11,12]*Ep1*volt,
    [13,14,15,]*Ep2*volt,
    []*Ep3*volt,
    [],
    [],
    [],
    [],
    [],
    Ep4 = 0;




]
0<c0<currentlimit
t

V=400
Ep1 = 100
Ep2 = 20
kvot = 5/60000
obj = [Ep1*V*kvot, Ep2*V*kvot]
#      ─┬  ─┬
#       │   └┤ Coefficient for y
#       └────┤ Coefficient for x

lhs_ineq = [[ 2,  1],  # Red constraint left side
             [-4,  5],  # Blue constraint left side
             [ 1, -2]]  # Yellow constraint left side

rhs_ineq = [20,  # Red constraint right side
            10,  # Blue constraint right side
            2]  # Yellow constraint right side

lhs_eq = [[V*kvot, v*kvot]]  # Green constraint left side
rhs_eq = [20]       # Green constraint right side

bnd = [(0, float("inf")),  # Bounds of x
      (0, float("inf"))]  # Bounds of y
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
            method="revised simplex")
print(opt)