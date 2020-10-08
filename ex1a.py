from data import *
from pulp import *
threshold=10
a=[]
for i in range(n):
        temp=[]
        for j in range(k):
                if(time[i][j]<=threshold):
                        temp.append(1)
                else:
                        temp.append(0)
        a.append(temp)
prob=LpProblem("Set_Covering_Problem", LpMinimize)
x=LpVariable.dicts("x",[i for i in range(k)],0,1,LpInteger)
prob += lpSum([x[i] for i in range(k)])
for i in range(n):
        prob += lpSum([x[j]*a[i][j] for j  in range(k)])>=1
prob.solve()
print value(prob.objective)
for v in prob.variables():
        print "{}={}".format(v.name,v.varValue)


