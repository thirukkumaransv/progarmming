aa=int(input())
bb=list(map(int,input().split(None,aa)[:aa]))
aa=[]
for i in range(len(bb)):
    if bb[i]==i:
        
        aa.append(bb[i])
if len(aa)==0:
    print(-1)
else:
    print(" ".join(map(str,aa)))
