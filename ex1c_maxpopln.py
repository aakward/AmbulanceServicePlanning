from pulp import *
from data import *

A=[[0 for i in range(40)] for j in range(85)]
for i in range (40):
   for j in range (85):
      if time[j][i] <= 10:
          A[j][i]=1
      else:
          A[j][i]=0

prob = LpProblem('Prob_1a',LpMaximize)


x = LpVariable.dicts('x',[i for i in range (40)],0,1,LpBinary)
y = LpVariable.dicts('y',[i for i in range (85)],0,1,LpBinary)

prob += lpSum(popln[i]*y[i] for i in range (85))

for j in range (85):
   prob += lpSum(A[j][i]*x[i] for i in range (40)) >= y[j]

prob += lpSum(x[i] for i in range (40)) <= 3

prob.writeLP('Prob_1a')
prob.solve()

for v in prob.variables():
    if v.varValue == 1:
        print(v.name)

print(value(prob.objective))
