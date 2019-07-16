e=int(input())
f=[]
g=0
for i in range(0,e):
    f.append(i)
for j in range(len(f)):
    for k in range(j+1,len(f)):
        g+=1
print(g)
