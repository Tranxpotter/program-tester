import sys
sys.tracebacklimit=0
x=input().split()
num=len(x)
for i in range(num):
    if i%2==0:
        x[i]=int(x[i])
s=1
y=0
while s<num:
    if x[s]=="*":
        y=x[s-1]*x[s+1]
        x[s-1]=y
        x.pop(s)
        x.pop(s)
        num=num-2
    elif x[s]=="/":
        y=x[s-1]/x[s+1]
        x[s-1]=y
        x.pop(s)
        x.pop(s)
        num=num-2
    else:
        s=s+2
s=1
while num!=1:
    if x[s]=="+":
        y=x[s-1]+x[s+1]
        x[s-1]=y
        x.pop(s)
        x.pop(s)
        num=num-2
    else:
        y=x[s-1]-x[s+1]
        x[s-1]=y
        x.pop(s)
        x.pop(s)
        num=num-2
print(float(x[0]))

        


       
