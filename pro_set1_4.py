m,n=map(str,input().split())
temp=0
if len(m)>len(n):
  m,n=n,m
p=0
while p<len(m):
  temp+=(ord(n[p])-ord(m[p]))
  p+=1
for p in range(p,len(n)):
  temp+=ord(n[p])-ord('a')+1
print(temp)
