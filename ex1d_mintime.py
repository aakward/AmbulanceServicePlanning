from pulp import *
from data import *


A=[[0 for i in range(40)] for j in range(85)]
for i in range (40):
   for j in range (85):
      if time[j][i] <= 10:
          A[j][i]=1
      else:
          A[j][i]=0

B=[[0 for i in range(40)] for j in range(85)]
for i in range (40):
   for j in range (85):
      if time[j][i] <= 10:
          B[j][i]=time[j][i]
      else:
          B[j][i]=0

prob = LpProblem('Prob_1a',LpMinimize)


x = LpVariable.dicts('x',[i for i in range (40)],0,1,LpBinary)

prob += lpSum((B[j][i]*x[i] for i in range (40)) for j in range (85))

for j in range (85):
   prob += lpSum(A[j][i]*x[i] for i in range (40)) >= 1

prob += lpSum(x[i] for i in range (40)) <= 8

prob.writeLP('Prob_1a')
prob.solve()

print(value(prob.objective))
for v in prob.variables():
    if v.varValue == 1:
        print(v.name)

