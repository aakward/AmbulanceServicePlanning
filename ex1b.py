import matplotlib.pyplot as plt
from data import *
from pulp import *
obj=[]
for l in range(len(threshold)):
        a=[]
        for i in range(n):
                temp=[]
                for j in range(k):
                        if(time[i][j]<=threshold[l]):
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
        obj.append(value(prob.objective))
plt.plot(threshold,obj,'ro')
plt.xlabel("Thresholds")
plt.ylabel("No. of Ambulances")
plt.title("Plot of optimal No. of Ambulances against Different Thresholds")
plt.show()
